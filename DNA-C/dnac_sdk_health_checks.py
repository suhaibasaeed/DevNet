from dnacentersdk import DNACenterAPI # import DNACenterAPI class
import json
import time

# Instantiate DNACenterAPI class passing in URL and credentials
# Does token handling for us
dna = DNACenterAPI(base_url='https://sandboxdnac2.cisco.com', username='devnetuser', password='Cisco123!')


############# CLIENTS ##############
#  Calculate epoch datetime in ms
epoch_datetime = int(time.time() * 1000)
# Invoke method to Get Client Health from clients class passing in epoch time
client_health = dna.clients.get_overall_client_health(timestamp=f"{epoch_datetime}")

print(json.dumps(client_health, indent=2, sort_keys=True))
print(' ')

# GET NETWORK HEALTH
net_health = dna.topology.get_overall_network_health(timestamp=f"{epoch_datetime}")
#
print(net_health)
print(' ')
# GET SITE HEALTH
site_health = dna.sites.get_site_health(timestamp=str(epoch_datetime))
print(json.dumps(site_health, indent=2, sort_keys=True))