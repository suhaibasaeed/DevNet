import requests
import json
"""
This python script pulls CDP neighbours info from a device using NX-API CLI then gets the
login token via NX_API REST and then configures descriptions on the devices interfaces based
on this CDP data
"""

# Authentication which will be passed into header
switchuser = 'admin'
switchpassword = 'Admin_1234!'
# URL, headers and payload passed into bodACy of POST request
url = 'https://sbx-nxos-mgmt.cisco.com/ins'
headers = {'content-type': 'application/json'}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show cdp nei",
        "output_format": "json"
    }
}
# HTTP post request passing in URL, payload, headers and authentication info
response = requests.post(url, data=json.dumps(
    payload), headers=headers, auth=(switchuser, switchpassword), verify=False).json()  # Convert to python dict

print(response)

########## LOGIN WITH NX-API REST ##################

# URL we hit to get the token
auth_url = "https://sbx-nxos-mgmt.cisco.com/api/mo/aaaLogin.json"
# JSON payload to pass into the body
auth_payload = {
    "aaaUser":{
        "attributes":{
            "name": "admin",
            "pwd": "Admin_1234!"
        }
    }
}

# POST request
auth_response = requests.post(auth_url, headers=headers, data=json.dumps(auth_payload), verify=False).json()

# Get token back from the JSON response
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
# Put token in cookies dictionary - We'll be using this in any further requests
cookies = {}
cookies['APIC-Cookie'] = token

counter = 0
# Get number of neighbours from the response
nei_count = response['ins_api']['outputs']['output']['body']['neigh_count']
print(nei_count)

# Loop through neighbours and get hostname, local and remote int from JSON cdp nei data
# Will only run if we actually have CDP neighbours
while counter < nei_count:
    # Go through records in the row and get info
    hostname = response['ins_api']['outputs']['output']['body'][
        'TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['device_id']
    local_int = response['ins_api']['outputs']['output']['body'][
        'TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['intf_id']
    # print(local_int)
    remote_int = response['ins_api']['outputs']['output']['body'][
        'TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['port_id']


    # Build payload based on the info extracted above
    body = {
        "l1PhysIf": {
            "attributes": {
                "descr": f'Connected to {hostname} Remote intf is {remote_int}'
            }
        }
    }
    counter += 1

    # We don't want to configure the mgmt0 intf so don't execute below code for that loop iter
    if local_int != 'mgmt0':
        # Format interface name to be like eth1/1
        int_name = local_int.lower().split("ernet")
        int_name = "".join(int_name)
        # Create URL we're posting to dynamically based on interface name
        int_url = f"https://sbx-nxos-mgmt.cisco.com/api/mo/sys/intf/phys-[{int_name}].json"

        # POST request
        post_response = requests.post(int_url, data=json.dumps(
            body), headers=headers, cookies=cookies, verify=False).json()
        print(post_response)