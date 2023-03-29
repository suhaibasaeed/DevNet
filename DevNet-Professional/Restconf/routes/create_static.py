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
    "Content-Type": "application/yang-data+json",
}
# Get the running configuration
url = f"https://{device['host']}:{device['port']}/restconf/data/native/ip/route"

# Read routes config from file
with open("route_config.yaml") as f:
    route_config = safe_load(f)

# Send POST request to create static routes
response = requests.put(url, auth=(device["username"], device["password"]), headers=headers, json=route_config, verify=False)

# Flag an error if the request fails
response.raise_for_status()

if response.ok:
    print("Static routes created successfully!")


