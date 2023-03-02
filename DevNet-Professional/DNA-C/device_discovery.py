import requests
import urllib3
from json import dumps
from rich.pretty import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://sandboxdnac.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

user = "devnetuser"
password = "Cisco123!"
# POST to get token
auth_response = requests.post(
    url=f"{base_url}{auth_endpoint}", auth=(user, password), verify=False
).json()
# Parse out token
token = auth_response["Token"]

# global credentials url
global_credentials_url = "intent/api/v1/global-credential?credentialSubType="

# GET request to get CLI creds
cli_creds_response = requests.get(
    url=f"{base_url}{global_credentials_url}CLI",
    headers={"X-Auth-Token": token},
    verify=False,
).json()

# GET request to get SNMP creds
snmp_creds_response = requests.get(
    url=f"{base_url}{global_credentials_url}SNMPV2_WRITE_COMMUNITY",
    headers={"X-Auth-Token": token},
    verify=False,
).json()
# Parse out the IDs
cli_cred_id = cli_creds_response["response"][0]["id"]
snmp_cred_id = snmp_creds_response["response"][0]["id"]

payload = {
    "name": "Fusion Router Discovery",
    "discoveryType": "Range",
    "ipAddressList": "192.168.1.5-192.168.1.6",
    "timeout": 1,
    "protocolOrder": "ssh, telnet",
    "preferredMgmtIPMethod": "None",
    "globalCredentialIdList": [cli_cred_id, snmp_cred_id],
}

# POST to create a discovery
discovery_endpoint = "intent/api/v1/discovery"

discovery_response = requests.post(
    url=f"{base_url}{discovery_endpoint}",
    headers={"X-Auth-Token": token},
    data=dumps(payload),
    verify=False,
    ).json()