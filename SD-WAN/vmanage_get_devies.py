import requests
import json
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # turn off SSL warning

# URL we're hitting
url = "https://10.10.20.90:8443/j_security_check"
# Body will be a python dict not JSON as usual
login_body = {
    'j_username': 'admin',
    'j_password': 'C1sco12345'
}

# We use a session for SD-WAN login which is instantiated here - Done so we can get the cookie back and store it
session = requests.session()

# Note how we dont use json.dumps as it is passed in as python dict
response = session.post(url, data=login_body, verify=False)

# The response will always come back 200 OK even if auth failed so we need to deal with this case
# If the response has any text in it then it has failed
if response.status_code != 200 or response.text:
    print("Login has failed - Exiting script")
    sys.exit(1)
# Authentication was otherwise successful
else:
    print("Authentication was successful")

# New URL to get the device data
device_url = "https://10.10.20.90:8443/dataservice/device"

# Notice how we are using session again and not requests
device_response = session.get(device_url, verify=False).json()

# Loop through the returned list of device data and print it's details
for device in device_response["data"]:
    print(f"The device hostname is {device['host-name']} at site ID {device['site-id']}")
    print(f"The device IP is {device['system-ip']}")
    print(f"The device status is {device['status']}")
    print("*" * 40)