import requests
import json
# URL we're hitting to get the details of a particular device
url = "https://10.10.20.49:443/restconf/data/tailf-ncs:devices/device=dist-rtr01"
auth = ("developer", "C1sco12345")
# Headers we're passing in
headers = {'Accept': 'application/yang-data+json'}
# Get request passing in URL, credentials, headers and don't check SSL cert
response = requests.get(url, auth=auth, headers=headers, verify=False).json()
# Parse to get to the inner dictionary
response = response["tailf-ncs:device"][0]
# Print device details
print(f"The device hostname is {response['name']} with the IP: {response['address']}")
print(f"Model is {response['platform']['model']} running {response['platform']['name']}")



