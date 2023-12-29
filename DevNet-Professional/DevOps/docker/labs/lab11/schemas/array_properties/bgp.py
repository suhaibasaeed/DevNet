from ..objects.ip import IP_OBJECT
from ..objects.bgp import BGP_NEIGHBOR_OBJECT

BGP_NEIGHBOR_PROPERTY = {
    "type": "array",
    "items": BGP_NEIGHBOR_OBJECT,
    "uniqueItems": True,
}
"""
EX:
[
    {
        "ip": "10.1.2.1",
        "remote_as": 65002
    }
]
"""

BGP_ADVERTISED_NETWORK_PROPERTY = {
    "type": "array",
    "items": IP_OBJECT,
    "uniqueItems": True,
}
"""
EX:
[
    {
        "ip": "10.1.10.0",
        "mask": 24
    }
]
"""
