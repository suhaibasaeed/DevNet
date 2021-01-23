import requests
from pprint import pprint
from json import dumps

# URL we hit to get the token
url = "https://sbx-nxos-mgmt.cisco.com/api/mo/aaaLogin.json"
# JSON payload to pass into the body
payload = {
    "aaaUser":{
        "attributes":{
            "name": "admin",
            "pwd": "Admin_1234!"
        }
    }
}

headers = {
  'Content-Type': 'application/json',
}
# POST request
response = requests.post(url, headers=headers, data=dumps(payload), verify=False).json()

# Get token back from the JSON response
token = response['imdata'][0]['aaaLogin']['attributes']['token']

# Put token in cookies dictionary - We'll be using this in any further requests
cookies = {}
cookies['APIC-Cookie'] = token

# Change URL so to interface one so we can change the description
url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/38].json"

# Change payload to what we're changing desc to
payload = {
    "l1PhysIf":{
        "attributes":{
            "descr":"SAS woz ere"
        }
    }
}
# Pass in URL, payload, headers, cookies with token it in and don't check SSL cert
put_response = requests.put(url, data=dumps(payload), headers=headers, cookies=cookies, verify=False)
# Get back JSON and print
put_response = put_response.json()
pprint(put_response)

