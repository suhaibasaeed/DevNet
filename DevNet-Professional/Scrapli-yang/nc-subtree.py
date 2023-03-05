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
# Hierarchy to filter on
ospf_filter = """
<ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
  <ospf-state>
    <ospf-instance>
      <af>address-family-ipv4</af>
      <router-id>167837953</router-id>
        <ospf-area>
            <area-id>0</area-id>
            <ospf-interface>
                <name>GigabitEthernet2</name>
                  <ospf-neighbor>
                    <neighbor-id>10.1.1.2</neighbor-id>
                  </ospf-neighbor>
            </ospf-interface>
        </ospf-area>
    </ospf-instance>
  </ospf-state>
</ospf-oper-data>
"""
# Open connection to device
with NetconfDriver(**device) as conn:

    # Pass in filter and filter type
    response = conn.get(filter_=ospf_filter, filter_type="subtree")

    print(response.result)
