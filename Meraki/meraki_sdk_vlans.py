from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from pprint import pprint
from json import dumps
# Meraki API key
api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

# Create MerakiSdkClient object and pass in the api key
meraki = MerakiSdkClient(api_key)

# Get organisations by calling method on organizations class
orgs = meraki.organizations.get_organizations()

# Loop through organisations and ge the id of the DevNet Sandbox org
for org in orgs:
    if org["name"] == "DevNet Sandbox":
        org_id = org["id"]

# Get the networks in DevNet Sandbox org
params = {"organization_id": org_id}
# Get networks by calling method on networks class and sass in org_id as dict as this is format API wants
networks = meraki.networks.get_organization_networks(params)

# Loop through networks and get the network id of the DevNet Sandbox always on network
for network in networks:
    if network["name"] == 'DevNet Sandbox ALWAYS ON':
        network_id = network["id"]

# Get the vlans of this network by calling method on vlans class and passing in network_id
vlans = meraki.vlans.get_network_vlans(network_id)

# Get rid of outer one element list of vlans - This dict will be passed into the update_network_vlan method later
vlan = vlans[0]

# Update the name of the default vlan
vlan['name'] = "SAS was ere"
# dictionary that will have the network, vlan id and original dict of the VLAN we're changing
updated_vlan = {}
updated_vlan["network_id"] = network_id
updated_vlan["vlan_id"] = vlan["id"]
updated_vlan["update_network_vlan"] = vlan # VLAN dictionary we we're returned

# Update name of VLAN 1 via calling update_network_vlan on vlans class
result = meraki.vlans.update_network_vlan(updated_vlan)

# Verify the result
result_vlans = meraki.vlans.get_network_vlans(network_id)
pprint(result_vlans)

