import requests
import xml.dom.minidom as xm # Used to parse and make XML pretty
import xmltodict # XML being used instead to JSON
import urllib3
import json

# Suppress insecure warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#### For use with the DevNet Sandbox CUCM 11.5 #####
# URL of the server
url = 'https://10.10.20.1/cucm-uds/users'
#
headers = {
    'Accept': 'application/xml',
    'Content-Type': 'application/xml'
}
# Credentials
username = 'administrator'
pw = 'ciscopsdt'
# GET request passing in the URL and credentials for Basic auth
r = requests.get(url, auth=(username, pw), verify=False)

# Pretty up the XML response
tree = xm.parseString(r.text) # Parse XML text
pretty = tree.toprettyxml() # Call topretty() method on tree object

# Convert the pretty xml to a python dict
xmldata = xmltodict.parse(pretty)
print(json.dumps(xmldata, indent=2, sort_keys=True))
# Get inner data structure with the list of users
users = xmldata['users']['user']
# Loop through the list of users and print Name and ID
for user in users:
    print(f"{user['lastName']} {user['firstName']}")
    print(f"ID: {user['id']}")
    print(" ")
