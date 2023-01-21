import requests
import json

# Get your token here after logging in: https://developer.webex.com/docs/api/getting-started
token = 'YTlmNmI3Y2UtNGZiOS00MWI4LTgyYWYtOGJlNmIyY2RiZjMxNjdmN2RjODYtMzZl_PE93_cb22bf91-b84e-4c50-ab49-cd704940b921'


# URL we're hitting
url = 'https://webexapis.com/v1/teams'
# Headers inc credentials in form of bearer token
headers = {'Authorization': f'Bearer {token}', # Pass in token to header
           'Content-Type': 'application/json'}

# GET request so we can verify the team was actually created
get_response = requests.get(url, headers=headers).json()

# Get teamID by parsing through response - Needed so room is associated with Team
teamId = get_response['items'][0]["id"]


###### CREATE A ROOM ########
room_url = 'https://webexapis.com/v1/rooms'
# payload with name and ID of the team it is associated with
room_body = {
    "title": "Suhaib's Room",
    "teamId": teamId
}

# POST request passing in URL, headers and payload
room_post = requests.post(room_url, headers=headers,data=json.dumps(room_body)).json()
# GET request to confirm creation of the room
get_rooms = requests.get(room_url, headers=headers).json()
# Retreive the unique ID of the room - will be used later when we're posting a message to the team
room_id = get_rooms['items'][0]['id']

print(f"The team with ID {teamId} has a room with ID {room_id}")

#### POST A MESSAGE TO THE ROOM ####
msg_url = 'https://webexapis.com/v1/messages'
# Payload with room_id of the one we created above
msg_body = {
    "roomId": room_id,
    'text': 'ALERT: Interface on device XYZ is down' # Message we want to send to the room
}
# POST request passing in the URL, headers and payload
msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_body)).json()
