from .properties.bgp import BGP_AS_PROPERTY
from .array_properties.bgp import (
    BGP_NEIGHBOR_PROPERTY, BGP_ADVERTISED_NETWORK_PROPERTY
)


BGP_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "local_as": BGP_AS_PROPERTY,
        "neighbors": BGP_NEIGHBOR_PROPERTY,
        "advertised_networks": BGP_ADVERTISED_NETWORK_PROPERTY,
    },
    "required": ["local_as", "neighbors", "advertised_networks"]
}
"""
EX:
{
    "local_as": 65001,
    neighbors: [
        {
            "ip": 10.1.2.1",
            "remote_as": 65002
        }
    ],
    "advertised_networks": [
        {
            "ip": 10.1.10.0",
            "mask": 24
        }
    ]
}
"""
