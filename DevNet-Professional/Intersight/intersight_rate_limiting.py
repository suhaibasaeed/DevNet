from requests.adapters import HTTPAdapter
from requests import Session
from urllib3.util.retry import Retry
from intersight_auth import IntersightAuth
from rich import print
from dotenv import load_dotenv
import os
import requests

load_dotenv()

base_url = "https://www.intersight.com/api/v1/"

# Create session object - Allows us to persist certain parameters across requests
session = Session()
# Create retry object passing in details about retries and codes/methods we want to retry
retries = Retry(
    total=3, status_forcelist=[429, 500, 502, 503, 504], method_whitelist=["HEAD", "GET", "OPTIONS"]
)
# Call mount method on session object and pass in base_url and HTTPAdapter object wiht retries obj
session.mount(base_url, HTTPAdapter(max_retries=retries))


# Specify the API key and private key file
api_key = os.environ.get("INTERSIGHT_KEY")
private_key = os.environ.get("INTERSIGHT_SECRET_FILE")

# Create an instance of the IntersightAuth class
auth = IntersightAuth(secret_key_filename=private_key, api_key_id=api_key)

# get network elements
get_url = "https://www.intersight.com/api/v1/network/Elements"
# Use session object instead of usual requests
get_request = session.get(get_url, auth=auth)
get_request.raise_for_status()

print(get_request.json())