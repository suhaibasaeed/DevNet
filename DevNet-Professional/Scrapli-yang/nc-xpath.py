from scrapli_netconf.driver import NetconfDriver

device = {
    "host": "192.168.1.108",
    "auth_username": "admin",
    "auth_password": "admin",
    "auth_strict_key": False,
    "port": 830,
    # Make it work with Windows
    "transport": "paramiko",
}

rpc_filter = '''
<get>
<filter xmlns:t="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper" type="xpath select="/ospf-oper-data/ospf-state/ospf-instance[af='address-family-ipv4' and router-id='167837953']/ospf-area[area-id=0]/ospf-interface[name='GigabitEthernet2']/ospf-neighbor[neighbor-id='10.1.1.2']"/>
</get>

'''

# Open connection to device
with NetconfDriver(**device) as conn:
    
    response = conn.rpc(rpc_filter)

    print(response.result)
