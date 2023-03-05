import requests
import urllib3
from json import dumps
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

# URL for client health
client_health_endpoint = "intent/api/v1/client-health"

# GET to get client health
client_health_response = requests.get(
    url=f"{base_url}{client_health_endpoint}",
    headers={"X-Auth-Token": token},
    verify=False,
).json()

scores = client_health_response["response"][0]["scoreDetail"]

for score in scores:
    print(
        f"{score['scoreCategory']['value']} has {score['clientCount']} clients connected"
    )
