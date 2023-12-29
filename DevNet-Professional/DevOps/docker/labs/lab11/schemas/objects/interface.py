from ..properties.interface import (
    INTERFACE_ZONE_PROPERTY, INTERFACE_SECURITY_LEVEL_PROPERTY
)
from .ip import IP_OBJECT


INTERFACE_ZONE_OBJECT = {
    "type": "object",
    "properties": {
        "name": INTERFACE_ZONE_PROPERTY,
        "security_level": INTERFACE_SECURITY_LEVEL_PROPERTY,
    },
    "required": ["name", "security_level"],
    "additionalProperties": False,
}
"""
EX:
{
    "zone": {
        "name": "inside",
        "security_level": 100
    }
}
"""

INTERFACE_OBJECT = {
    "type": "object",
    "properties": {
        "zone": INTERFACE_ZONE_OBJECT,
        "ip_address": IP_OBJECT,
    },
    "required": ["ip_address"],
    "additionalProperties": False,
}
"""
EX:
{
    "zone": {
        "name": "inside",
        "security_level": 100
    },
    "ip_address": {
        "ip": "10.1.1.0",
        "mask": 24
    }
}
"""
