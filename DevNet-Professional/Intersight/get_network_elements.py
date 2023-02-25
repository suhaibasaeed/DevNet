import os
import requests
from intersight_auth import IntersightAuth
from rich import print
from dotenv import load_dotenv

load_dotenv()
# Specify the API key and private key file
api_key = os.environ.get("INTERSIGHT_KEY")
private_key = os.environ.get("INTERSIGHT_SECRET_FILE")

# Create an instance of the IntersightAuth class
auth = IntersightAuth(secret_key_filename=private_key, api_key_id=api_key)

# get network elements
get_url = "https://www.intersight.com/api/v1/network/Elements"
get_request = requests.get(get_url, auth=auth)

print(get_request.json())

