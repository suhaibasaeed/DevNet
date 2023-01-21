import requests
import json
from pprint import pprint
# URL we're hitting and credentials
url = "https://sbx-nxos-mgmt.cisco.com/ins"
switchuser = "admin"
switchpassword = "Admin_1234!"
# HTTP headers
myheaders = {"content-type": "application/json"}
# Payload which goes inside body of the request
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show version", # Send show version to device
        "output_format": "json",
    }
}
# POST operation passing in URL, body, headers, credentials and don't check SSL cert
response = requests.post(
    url,
    data=json.dumps(payload), # serialise to JSON
    headers=myheaders,
    auth=(switchuser, switchpassword),
    verify=False,
)

# Deserialise into python dictionary
api_data = response.json()

api_data = api_data["ins_api"]["outputs"]["output"]["body"]

hostname = api_data["host_name"]

print(f"The hostname of this device is {hostname}")