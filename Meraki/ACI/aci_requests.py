import requests
from pprint import pprint
from json import dumps

# URL we hit to get the token
url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"
# JSON payload to pass into the body
payload = {
    "aaaUser":{
        "attributes":{
            "name": "admin",
            "pwd": "ciscopsdt"
        }
    }
}

headers = {
  'Content-Type': 'application/json',
}
# POST request passing in URL, payload, and don't check SSL cert. Change json to python dict
response = requests.post(url, headers=headers, data=dumps(payload), verify=False).json()

# Get token back from the JSON response
token = response['imdata'][0]['aaaLogin']['attributes']['token']

# Put token in cookies dictionary - We'll be using this in any further requests
cookies = {}
cookies['APIC-Cookie'] = token


# Get application profile
app_url = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-web-tentant/ap-web-ap.json"

headers = {
    "cache_control": "no-cache"
}

# Send GET request and pass in token via cookies dict
app_response = requests.get(app_url, headers=headers, cookies=cookies, verify=False).json()

# Update the description on the application profile
post_payload = {
    "fvAp": {
                "attributes": {
                    "descr": "test",
                    "dn": "uni/tn-web-tentant/ap-web-ap"
        }
    }
}
# POST request passing in same URL, headers, token, payload and don't check SSL cert
post_response = requests.post(app_url, headers=headers, cookies=cookies, data=dumps(post_payload), verify=False).json()

# Send GET request again to verify description was actually updated
app_response = requests.get(app_url, headers=headers, cookies=cookies, verify=False).json()

print(dumps(app_response, indent=2))
