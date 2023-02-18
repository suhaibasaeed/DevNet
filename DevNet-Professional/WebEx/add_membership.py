import requests
from json import dumps

# Get your token here after logging in: https://developer.webex.com/docs/api/getting-started
token = "xxx"

# URL we're hitting to hit rooms
url = "https://webexapis.com/v1/rooms"
# Headers inc credentials in form of bearer token
headers = {"Authorization": f"Bearer {token}"}

# GET request so we can verify the team was actually created
get_response = requests.get(url, headers=headers).json()

# Loop through rooms and get ID of the ones with suhaib in the title
for room in get_response["items"]:
    if 'Marketing' in room["title"] or 'Random' in room["title"]:
        room_id = room["id"]
        
        # URL we're hitting for memberships
        membership_url = "https://webexapis.com/v1/memberships"
        # Headers and body for the POST request
        membership_headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        # Person email is what we got when we created the bot
        membership_body = {"roomId": room_id, "personEmail": "cbtbot@webex.bot", "isModerator": False}

        # POST request to add the bot to the room
        post_response = requests.post(membership_url, headers=membership_headers, data=dumps(membership_body))

        # Raise errors
        post_response.raise_for_status()

        if post_response.status_code == 200:
            print(f"Bot added successfully to room {room['title']}")

        
