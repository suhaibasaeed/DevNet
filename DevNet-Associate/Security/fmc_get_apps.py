import json
import sys
import requests

# Set up URLs and headers
login_url = 'https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/auth/generatetoken'
headers = {'Content-Type': 'application/json'}
# Credentials passed to URL so we can get the token
user = 'saeed.suha'
pw = 'tfcHAvWf'

# POST the username and password to the login endpoint
login_response = requests.post(login_url, auth=(user, pw), verify=False)

# Parse out the headers as the token is in here
resp_headers = login_response.headers

# Grab the token from the response headers by looking for the X-auth-access-token key
token = resp_headers.get('X-auth-access-token', default=None)
# If the token field is empty exit the program
if token == None:
    print('Failed to get a token. Try again')
    sys.exit()

# Set the token in the headers to be used in the next call
headers['X-auth-access-token'] = token

# URL for monitored apps
apps_url = 'https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/applications'

# Get list of montiored apps passing in URL, headers inc token and turn off SSL cert verification
apps_response = requests.get(apps_url, headers=headers, verify=False).json()
print(json.dumps(apps_response, indent=2, sort_keys=True))
