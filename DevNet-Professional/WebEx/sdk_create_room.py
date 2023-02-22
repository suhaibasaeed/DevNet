from webexteamssdk import WebexTeamsAPI

# Create a Webex Teams API access object
api = WebexTeamsAPI(access_token="xxx")

# Create room called "My Room"
room = api.rooms.create("My Room")

# Send message to room
api.messages.create(room.id, text="Hello World!")
