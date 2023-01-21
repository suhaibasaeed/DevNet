import requests
import json

# Login details - URL and username + password used to get token
base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"
user = 'devnetuser'
pw = 'Cisco123!'

# Send POST request passing in URL, username and password and covert to python dict
response = requests.post(url=f"{base_url}{auth_endpoint}", auth=(user, pw)).json()
# Parse token out of the response
token = response['Token']

#GET CLIENT HEALTH STATS
# URL which will be appended to end of the base_url
health_url = "intent/api/v1/client-health"
# Query string to pass in as parameters
querystring = {"timestamp": ""}
# Headers with token we parsed earlier
headers = {
    'x-auth-token': token,
    'Accept': "application/json"
}

# GET request passing in client health URL, headers, and params for querystring
response = requests.get(url=f"{base_url}{health_url}", headers=headers, params=querystring).json()

# Print the number of clients
print(f"Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")

# Get the inner data structure with the different type of client score categories
scores = response['response'][0]['scoreDetail']

# Loop through the different score categories i.e. all, wired and wireless
for score in scores:
    # If it's wired then print the amount of wired clients and then print the no. of client with each score i.e. fair
    if score['scoreCategory']['value'] == 'WIRED':
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values: # Loop through each score i.e fair, poor and good etc
            # Print name and amount of clients
            print(f"{score_value['scoreCategory']['value']}: {score_value['clientCount']}")
    #If it's's wireless then print the amount of wireless clients & print the no. of clients with each score
    elif score['scoreCategory']['value'] == 'WIRELESS':
        print(f"Wireless Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values: # Loop through each score i.e fair, poor and good etc
            print(f"{score_value['scoreCategory']['value']}: {score_value['clientCount']}")