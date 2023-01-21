import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Base URL as well as login URL
url = "https://fmcrestapisandbox.cisco.com"
login_url = '/api/fmc_platform/v1/auth/generatetoken'
headers = {'Content-Type': 'application/json'}
# Credentials to get the token
user = 'saeed.suha'
pw = 'bzWqpeK6'

# Send POST request passing in the combined URL, credentials and don't check SSL cert
login_response = requests.post(f'{url}{login_url}', auth=(user, pw), verify=False)
# Parse out the headers from the response as token in not in body but in headers
resp_headers = login_response.headers
# Grab the token from the response headers dictionary
token = resp_headers.get('X-auth-access-token', default=None)
# Set the token in the headers to be used in the next call
headers['X-auth-access-token'] = token

# URL we need to hit to create access policy
policy_url = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies"
# Payload we're passing into the body
payload = {
"type": "AccessPolicy",
"name": "SAS Enterprise Corporate AC Policy ",
"description": "SAS demo policy",
"defaultAction": {
 "intrusionPolicy": {
   "name": "Security Over Connectivity",
   "id": "abba9b63-bb10-4729-b901-2e2aa0f4491c",
   "type": "IntrusionPolicy"
 },
 "variableSet": {
   "name": "Default Set",
   "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
   "type": "VariableSet"
 },
 "type": "AccessPolicyDefaultAction",
 "logBegin": False,
 "logEnd": True,
 "sendEventsToFMC": True # Gives us logging whenever event triggered
}
}

# Send POST request to endpoint passing in the combined policy URL, headers w/ token, payload, and don't check SSL cert
policy_response = requests.post(f"{url}{policy_url}", headers=headers, data=json.dumps(payload), verify=False).json()
print(json.dumps(policy_response, indent=2))
print("Policy has been successfully created")

# Retreive the policy ID from the response
policy_id = policy_response["id"]
print(policy_id)

# API endpoint we need to hit to create access rules inside the policy
rules_url = f"https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/{policy_id}/accessrules"
# Add rules to monitor files for malware

# Payload we're passing in to create rules for policy - Taken from DevNet learning lab
rules_payload = {
  "sendEventsToFMC": True,
  "action": "ALLOW", # Allow traffic
  "enabled": True,
  "type": "AccessRule",
  "name": "Malware Inspect",
  "logFiles": True,
  "logBegin": False,
  "logEnd": False,
  "variableSet": {
    "name": "SAS DPI Malware rule",
    "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
    "type": "VariableSet"
  },
  "sourceNetworks": {
    "objects": [{
      "type": "NetworkGroup",
      "name": "IPv4-Private-All-RFC1918", # Run scanning from all private IPs
      "id": "15b12b14-dace-4117-b9d9-a9a7dcfa356f"
    }]
  },
  "filePolicy": {
    "name": "New Malware", # We're creating file policy called New Malware
    "id": "59433a1e-f492-11e6-98fd-84ec1dfeed47",
    "type": "FilePolicy"
  }
}
# POST request to create access rules
rules_resp = requests.post(rules_url, headers=headers, data=json.dumps(rules_payload), verify=False).json()

print(json.dumps(rules_resp, indent=2))
print("Rules successfully created")


