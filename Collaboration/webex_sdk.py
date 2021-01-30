from webexteamssdk import WebexTeamsAPI # Import class

# Create API object by instantiating class and passing in our access token
api = WebexTeamsAPI(access_token='YTlmNmI3Y2UtNGZiOS00MWI4LTgyYWYtOGJlNmIyY2RiZjMxNjdmN2RjODYtMzZl_PE93_cb22bf91-b84e-4c50-ab49-cd704940b921')

#### GET TEAM INFO ###
# Get a list of the teams in the form of team class object
teams = api.teams.list()
# Loop through the teams in the object
for team in teams:
    # As its an object we can check if it its team attribute is equal to the one we've already created
    if getattr(team, 'name') != 'Suhaib ':  # Create team if it doesn't exist
        create_team = api.teams.create('Team Suhaib')
        teamId = getattr(create_team, 'id') # Get the team ID by trying to get the respective attribute
    else:
        # If it already exists then just reference id attibute to get team id
        teamId = team.id

###### PEOPLE #####
print(api.people.me()) # Print out details about me
print(api.people.list())
# Create a new person with the role of administrator - roles string was retrieved from roles section below
api.people.create(emails=['email_here'], displayName='Suhaib Saeed', firstName='Suhaib',
                  lastName='Saeed', roles=['Y2lzY29zcGFyazovL3VzL1JPTEUvaWRfZnVsbF9hZG1pbg'])

#### ROLES #####
# Get the list of roles and print
roles = api.roles.list()
for role in roles:
    print(roles)

#### ROOMS #####
# Get the list of rooms
rooms = api.rooms.list()
evaluator = False
# Loop through rooms and check if ours already exists - if it does get the room id
for room in rooms:
    if room.title == 'Suhaibs Room':
        evaluator = True
        roomId = room.id
# If the room doesn't exist then create it, passing in the team ID - Also get the room ID
if evaluator == False:
    new_room = api.rooms.create('Suhaibs Room', teamId=teamId)
    roomId = new_room.id

#### MESSAGES ####
# post a message in the room passing in the roomID
api.messages.create(roomId, text='Posted from the SDK')

