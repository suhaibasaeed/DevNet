from ..properties.ip import IP_PROPERTY
from ..properties.bgp import BGP_AS_PROPERTY


BGP_NEIGHBOR_OBJECT = {
    "type": "object",
    "properties": {
        "ip": IP_PROPERTY,
        "remote_as": BGP_AS_PROPERTY,
    },
    "required": ["ip", "remote_as"],
    "additionalProperties": False,
}
"""
EX:
{
    "ip": "10.1.2.1",
    "remote_as": 65002
}
"""
