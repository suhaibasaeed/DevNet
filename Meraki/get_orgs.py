import requests
from pprint import pprint
import meraki

# URL we're hitting to get back list of organisations
url = "https://dashboard.meraki.com/api/v0/organizations/"

# API key in the headers
headers = {
  'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}
# GET request
response = requests.get(url, headers=headers)
# Get back JSON
data = response.json()

# Loop through organisations returned and get org ID of the DevNet Sanbox org
for org in data:
    if org["name"] == "DevNet Sandbox":
        org_id = org["id"]

# URL to get list of networks in the DevNet Sandbox organisation
network_url = f"https://dashboard.meraki.com/api/v0/organizations/{org_id}/networks"
# GET request and get back JSON
network_response = requests.get(network_url, headers=headers).json()

pprint(network_response)