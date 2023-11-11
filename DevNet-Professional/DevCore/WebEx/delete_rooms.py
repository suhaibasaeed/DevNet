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
    if "suhaib" in room["title"]:
        room_id = room["id"]

        # New room URL
        room_url = f"{url}/{room_id}"
        # DELETE request to delete the room
        delete_response = requests.delete(room_url, headers=headers)

        # Raise errors
        delete_response.raise_for_status()

        if delete_response.status_code == 204:
            print(f"Room {room['title']} was successfully deleted")
