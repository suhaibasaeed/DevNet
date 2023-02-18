import requests
from json import dumps
from sys import argv


def send_message(room_id, message):

    """Sends message to a room based on the room ID"""

    header = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    body = {"roomId": room_id, "text": message}

    post_response = requests.post(
        "https://webexapis.com/v1/messages", headers=header, data=dumps(body)
    )

    return post_response


# Bots token
token = "xxx"

# URL we're hitting to hit rooms
url = "https://webexapis.com/v1/rooms"
# Headers inc credentials in form of bearer token
headers = {"Authorization": f"Bearer {token}"}

message = argv[1]

# GET request to get all rooms the bot is in
get_response = requests.get(url, headers=headers).json()

# Loop through rooms and get ID of the ones with ALERTS in the title
for room in get_response["items"]:
    if "ALERTS" in room["title"]:
        room_id = room["id"]

        # Send message to the room
        send_message(room_id, message)
