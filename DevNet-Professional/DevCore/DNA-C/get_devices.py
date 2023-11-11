import requests
import urllib3
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

# GET request to get devices list
devices_endpoint = "intent/api/v1/network-device"

devices_response = requests.get(
    url=f"{base_url}{devices_endpoint}", headers={"X-Auth-Token": token}, verify=False
).json()

# Get single device ID
device_id = devices_response["response"][1]["id"]
# Get VLANs for device
device_vlan_endpoint = f"intent/api/v1/network-device/{device_id}/vlan"

device_response = requests.get(
    url=f"{base_url}{device_vlan_endpoint}",
    headers={"X-Auth-Token": token},
    verify=False,
).json()

pprint(device_response)
