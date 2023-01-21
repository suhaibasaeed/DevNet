from acitoolkit.acitoolkit import *

# URL and credentials
url = 'https://sandboxapicdc.cisco.com'
user = 'admin'
pw = 'ciscopsdt'

# Create the session object and pass in URL, username and password
session = Session(url, user, pw)

# Login to the session - deals with token part
session.login()

# Get tenants by calling get method on tenant object and passing in session
tenants = Tenant.get(session)
for tenant in tenants: # Loop through tenants list
    print(tenant.name)
    print(tenant.descr)
    print('*' * 30)
    print(' ')

# Create a new Tenant object and pass in name of new tenant
new_tenant = Tenant("Tenant_Name_Here")
new_tenant.get_url()
new_tenant.get_json()


# Create the application profile and the EPG objects
anp = AppProfile('Knoxs_app', new_tenant) # Pass in name and it's parent tenant name
epg = EPG('Knoxs_epg', anp) # Pass in name and parent object - anp here

# Create the L3 Namespace by creating Context and BridgeDomain objects
context = Context('Knoxs_VRF', new_tenant) # Pass in name and name of parent tenant
bridge_domain = BridgeDomain('Knoxs_bd', new_tenant)

# Associate the BD with the L3 Namespace i.e. Context
bridge_domain.add_context(context)
epg.add_bd(bridge_domain) # Associate epg to bridge domain

##### Tenant Creation is completed #####
print(new_tenant.get_url()) # Gives us URL API endpoint
print(new_tenant.get_json()) # Gives us body of post request
response = session.push_to_apic( # Push above data to the controller via POST
    new_tenant.get_url(), data=new_tenant.get_json())
print(response)
# Get list of tenants and print for verification
tenants = Tenant.get(session)
for tenant in tenants:
    if tenant.name == 'Tenant_Name_Here':
        print(tenant.name)
    else:
        print(tenant.name)
        print(tenant.descr)
        print('*' * 30)
        print(' ')
