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


# Get all network objects
get_url = "https://10.10.20.65/api/fdm/v6/object/networks"

get_headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}

while get_url:

    # Use pagination to only get 2 objects
    get_response = requests.get(
        get_url, headers=get_headers, params={"limit": 2}, verify=False
    )

    get_response.raise_for_status()

    data = get_response.json()

    # Print items in list
    for item in data["items"]:
        print(f"Item name {item['name']}")

    try:
        get_url = data["paging"]["next"][0]
        # If no next URL specified
        if not get_url:
            break

    # If list is empty
    except IndexError:
        break
