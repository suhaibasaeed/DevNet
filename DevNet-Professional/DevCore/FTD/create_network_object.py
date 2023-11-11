import requests
import json
from rich import print

# Disable SSL Warnings
requests.packages.urllib3.disable_warnings()

url = "https://10.10.20.65/api/fdm/v6/fdm/token"

# Body and headers for getting token
payload = {"grant_type": "password", "username": "admin", "password": "Sbxftd1234!"}
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# Get Token
token_response = requests.post(
    url, headers=headers, data=json.dumps(payload), verify=False
)

token_response.raise_for_status()
if token_response.status_code == 200:
    print("Token Successfully Received")
# Parse Token for later use
token = token_response.json()["access_token"]

# Endpoint for creating new object
url = "https://10.10.20.65/api/fdm/v6/object/networks"

payload = {
    "name": "SAS-DEV",
    "description": "DEVCOR",
    "subType": "NETWORK",
    "value": "99.99.99.0/24",
    "dnsResolution": "IPV4_ONLY",
    "type": "networkobject",
}
# Include token in headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}",
}

create_response = requests.post(
    url, headers=headers, data=json.dumps(payload), verify=False
)
create_response.raise_for_status()
if create_response.status_code == 200:
    print("[u]SUCCESS: New Object Created")
    print(create_response.text)
