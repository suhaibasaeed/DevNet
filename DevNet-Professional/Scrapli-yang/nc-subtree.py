from scrapli_netconf.driver import NetconfDriver
import xmltodict
from rich.pretty import pprint

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
</ospf-oper-data>
"""
# Open connection to device
with NetconfDriver(**device) as conn:

    # Pass in filter and filter type
    response = conn.get(filter_=ospf_filter, filter_type="subtree")

    # Convert XML to Python dictionary
    ospf_dict = xmltodict.parse(response.result)

    pprint(ospf_dict)
