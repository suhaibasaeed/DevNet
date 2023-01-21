import requests
import json
# IP of the ASA followed by URL for static routes
url = "https://172.16.1.131/api/routing/static"

# HTTP basic auth credentials
userpw = ('cisco', 'cisco')
# GET request passing in URL and credentials - Covert to python dicts and parse items key
get_response = requests.get(url, auth=userpw, verify=False).json()['items']

print(json.dumps(get_response, indent=2, sort_keys=True))