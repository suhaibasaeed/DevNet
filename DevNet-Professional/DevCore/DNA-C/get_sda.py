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
# Get list of device management IP addresses
device_mgmt_list = [
    device["managementIpAddress"] for device in devices_response["response"]
]

# Get SDA device info
sda_endpoint = "intent/api/v1/business/sda/device"
# Loop through device management IP addresses
for device_ip in device_mgmt_list:
    sda_response = requests.get(
        url=f"{base_url}{sda_endpoint}",
        headers={"X-Auth-Token": token},
        params={"deviceManagementIpAddress": device_ip},
        verify=False,
    ).json()

    pprint(sda_response)
