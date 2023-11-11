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
    # We are sending YANG data in JSON format
    "Content-Type": "application/yang-data+json",
}
# native/interface is part of the YANG model
url = f"https://{device['host']}:{device['port']}/restconf/data/native/interface"

# Read loopback interface from file
with open("loopconfig.yaml") as f:
    loopback_config = safe_load(f)

# Send POST request to create loopback interface
response = requests.post(url, auth=(device["username"], device["password"]), headers=headers, json=loopback_config, verify=False)

# Flag an error if the request fails
response.raise_for_status()

if response.ok:
    print("[green]Loopback interface created successfully[/green]")
    print(response.status_code)

