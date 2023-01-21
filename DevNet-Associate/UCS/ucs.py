from ucsmsdk.ucshandle import UcsHandle # Import class

# Create handle object by instantiating class and passing in the IP addr of server and credentials
handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")
# Login to the server
handle.login()

# return all objects of type OrgOrg i.e. get org info - Done by querying via class ID
org = handle.query_classid(class_id="orgOrg", hierarchy=True)
print(org)

# Return objects of type ComputedBlade i.e. server blade info
servers = handle.query_classid("computeBlade")
# Loop through objects and print server information
for server in servers:
    print(f"Server dn is {server.dn} - Has {server.num_of_cpus} no. of CPUs & memory: {server.available_memory}")

# Object query using a specific dn - i.e. a particular blade server
blade = handle.query_dn('sys/chassis-3/blade-1')
print(blade)
# Logout of the server
handle.logout()
