import requests
import json

# Get your token here after logging in: https://developer.webex.com/docs/api/getting-started
token = 'YTlmNmI3Y2UtNGZiOS00MWI4LTgyYWYtOGJlNmIyY2RiZjMxNjdmN2RjODYtMzZl_PE93_cb22bf91-b84e-4c50-ab49-cd704940b921'

### Create a Team ###
# URL we're hitting
url = 'https://webexapis.com/v1/teams'
# Headers inc credentials in form of bearer token
headers = {'Authorization': f'Bearer {token}', # Pass in token to header
           'Content-Type': 'application/json'}
# Name of the team we're creating
body = {
    "name": "Team Suhaib"
}

# POST request passing in URL, headers and body and convert into python dict
post_response = requests.post(url, headers=headers, data=json.dumps(body)).json()
print(post_response)

# GET request so we can verify the team was actually created
get_response = requests.get(url, headers=headers).json()

# Get inner data structure so we can loop through it
teams = get_response['items']
# Loop through teams and get ID of Team Suhaib - Will be used later when creating a room
for team in teams:
    if team['name'] == 'Team Suhaib':
        teamId = team['id']
print(f"The team created has the ID {teamId}")
