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

# URL for creating a site
create_site_endpoint = "intent/api/v1/site"

# body
data = {
        "type": "area",
        "site": {
            "area": {
                "name": "Illinois",
                "parentName": "Global"
            }
        }
}
# POST to create a site
create_site_response = requests.post(
    url=f"{base_url}{create_site_endpoint}",
    headers={"X-Auth-Token": token},
    data=dumps(data),
    verify=False,
).json()

pprint(create_site_response)
