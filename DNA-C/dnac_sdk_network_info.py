from dnacentersdk import DNACenterAPI # import DNACenterAPI class
import json

# Instantiate DNACenterAPI class passing in URL and credentials
# Does token handling for us
dna = DNACenterAPI(base_url='https://sandboxdnac2.cisco.com',
                       username='devnetuser', password='Cisco123!')

##### NETWORKS AND SITES ####

# Print Site Topology - Each site has an ID and parent ID if under another site
sites = dna.topology.get_site_topology()
# Loop through sites at highest level in hierarchy
for site in sites.response.sites: # We are referencing dict keys response & sites to get further into inner strcuture
    # Look for ID of the site called global (Top level site)
    if site.parentId == 'e95d9cef-2a00-4eb9-82df-01c3291410be':
        print(site.name)
        # Loop through the same list again to find child sites
        for child_sites in sites.response.sites:
            if child_sites.parentId == site.id: # If we find Site at 2nd level in hierachy
                print(f'{child_sites.name}')
            for more_children in sites.response.sites: # 3rd level down in hierarchy
                if more_children.parentId == child_sites.id and child_sites.parentId == site.id:
                    print(f'{more_children.name}')
    print(' ')

# Print Vlans by invoking method from topology class
vlans = dna.topology.get_vlan_details()
for vlan in vlans.response:
    print(vlan)

# Physical Topology Details
phys_top = dna.topology.get_physical_topology()
print(json.dumps(phys_top, indent=2, sort_keys=True))