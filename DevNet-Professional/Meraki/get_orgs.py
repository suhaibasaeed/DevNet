import requests
import dotenv
import os
import json
from rich.pretty import pprint

# Load environment variables from .env file
dotenv.load_dotenv()

# Set API key and base URL
token = os.environ.get("MERAKI_API_KEY")

base_url = "https://api.meraki.com/api/v1"

# Specify the headers inc token
headers = {
    "X-Cisco-Meraki-API-Key": token,
    "Content-Type": "application/json",
    "Accept": "application/json",
}

try:
    # Get list of orgs
    orgs_response = requests.get(f"{base_url}/organizations", headers=headers)

    if orgs_response.status_code == 200:
        orgs = orgs_response.json()

    for org in orgs:
        if org["name"] == "DevNet Sandbox":
            org_id = org["id"]

except Exception as e:
    print(e)

try:
    # Get list of networks in org
    networks_response = requests.get(f"{base_url}/organizations/{org_id}/networks", headers=headers)

    if networks_response.status_code == 200:
        networks = networks_response.json()
    
    for network in networks:
        if network["name"] == "CCNP-SABADO":
            network_id = network["id"]

except Exception as e:
    print(e)

print(f"CCNP-SABADO has Network ID {network_id}")
