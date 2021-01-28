from dnacentersdk import DNACenterAPI # import DNACenterAPI class


# Instantiate DNACenterAPI class passing in URL and credentials
# Does token handling for us
dna = DNACenterAPI(base_url='https://sandboxdnac2.cisco.com',
                       username='devnetuser', password='Cisco123!')
############### DEVICES #############
# Invoke method from devices class to get the list of devices
devices = dna.devices.get_device_list()
# Loop through the list of devices and print their details
for device in devices.response:
    print(device.type)
    print(device.hostname)
    print(device.managementIpAddress)
    print(device.id)
    print(" ")

# Get a specific device referencing it's unique ID
device = dna.devices.get_device_by_id('75d57d36-dade-40cb-aac3-b2267e7e0180')
print(device.response)

