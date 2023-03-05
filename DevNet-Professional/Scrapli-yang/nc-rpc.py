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

ospf_xpath = "ospf-oper-data/ospf-state/ospf-instance"

# Open connection to device
with NetconfDriver(**device) as conn:
    response = conn.get(filter_=ospf_xpath, filter_type="xpath")

    print(response.result)
