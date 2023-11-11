import requests
from yaml import safe_load
from rich import print

requests.packages.urllib3.disable_warnings()

device = {
    "host": "192.168.1.108",
    "port": 443,
    "username": "admin",
    "password": "admin",

}

headers = {
    # We want YANG data in JSON format
    "Accept": "application/yang-data+json",
}
# native/interface is part of the YANG model
url = f"https://{device['host']}:{device['port']}/restconf/data/native/interface"


# Send POST request to create loopback interface
response = requests.get(url, auth=(device["username"], device["password"]), headers=headers, verify=False)

# Flag an error if the request fails
response.raise_for_status()

print(response.text)



