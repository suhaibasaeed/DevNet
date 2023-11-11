import requests
import urllib3

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
