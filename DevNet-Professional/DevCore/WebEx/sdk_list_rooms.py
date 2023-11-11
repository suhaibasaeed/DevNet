from webexteamssdk import WebexTeamsAPI

# Create a Webex Teams API access object
api = WebexTeamsAPI(access_token="xxx")

# List rooms we're in
rooms = api.rooms.list()

# Loop through rooms and print
for room in rooms:
    print(room)
