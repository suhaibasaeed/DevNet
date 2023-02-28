import requests
import xmltodict

url = "https://10.10.20.110/nuova"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}
# creds in xml format
data = '<aaaLogin inName="ucspe" inPassword="ucspe"/>'

log_resp = requests.post(url, headers=headers, data=data)

log_resp.raise_for_status()
# convert xml to dict
log_output = xmltodict.parse(log_resp.text)

print(log_output)

