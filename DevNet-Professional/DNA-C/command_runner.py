import requests
import urllib3
from json import dumps
from rich.pretty import pprint
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://sandboxdnac.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

user = "devnetuser"
password = "Cisco123!"
# POST to get token
auth_response = requests.post(
    url=f"{base_url}{auth_endpoint}", auth=(user, password), verify=False
).json()
# Parse out token
token = auth_response["Token"]

device_endpoint = "intent/api/v1/network-device"

devices = requests.get(url=f"{base_url}{device_endpoint}", headers={"X-Auth-Token": token}, verify=False).json()

device_ids = [device["id"] for device in devices["response"]]

payload = {
    "commands": ["show version", "show ip int brief"],
    "deviceUuids": device_ids,
}

command_endpoint = "intent/api/v1/network-device-poller/cli/read-request"

command_response = requests.post(url=f"{base_url}{command_endpoint}", headers={"X-Auth-Token": token}, data=dumps(payload), verify=False).json()

task_response = requests.get(url=f"{base_url}intent/api/v1/task/{command_response['response']['taskId']}", headers={"X-Auth-Token": token}, verify=False).json()

# While we haven't got a response wait for a few seconds and try again
while task_response["response"]["progress"] == "CLI Runner request creation":

    task_response = requests.get(url=f"{base_url}intent/api/v1/task/{command_response['response']['taskId']}", headers={"X-Auth-Token": token}, verify=False).json()

    time.sleep(5)
    print("Waiting for response")


pprint(task_response["response"]["progress"])

# GET request for file passing in fileID
file_response = requests.get(url=f"{base_url}intent/api/v1/file/{task_response['response']['progress']['fileId']}", headers={"X-Auth-Token": token}, verify=False).json()

print(file_response.content)

# Write to file
with open("command_output.txt", "wb") as f:
    f.write(file_response.content)
