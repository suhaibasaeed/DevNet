import requests
from rich.pretty import pprint

# Get your token here after logging in: https://developer.webex.com/docs/api/getting-started
token = "xxx"

# URL we're hitting to hit rooms
url = "https://webexapis.com/v1/rooms"
# Headers inc credentials in form of bearer token
headers = {"Authorization": f"Bearer {token}"}

# GET request so we can verify the team was actually created
get_response = requests.get(url, headers=headers).json()

pprint(get_response)
