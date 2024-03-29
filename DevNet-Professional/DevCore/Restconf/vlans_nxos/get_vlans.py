import requests
from yaml import safe_load
from rich import print

requests.packages.urllib3.disable_warnings()

device = {
    "host": "192.168.1.197",
    "port": 443,
    "username": "admin",
    "password": "admin",

}

headers = {
    # We want YANG data in JSON format
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
# Get the running configuration
url = f"https://{device['host']}:{device['port']}/restconf/data/native/vlan"

# Send POST request to create loopback interface
response = requests.get(url, auth=(device["username"], device["password"]), headers=headers, verify=False)

# Flag an error if the request fails
response.raise_for_status()

print(response.text)


