from .objects.interface import INTERFACE_OBJECT


INTERFACE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "patternProperties": {
        r"^[A-Z].+\d": INTERFACE_OBJECT,
    },
    "additionalProperties": False,
}
"""
EX:
{
    "GigabitEthernet0/0": {
        "zone": {
            "name": "inside",
            "security_level": 100
        },
        "ip_address": {
            "ip": "10.1.1.0",
            "mask": 24
        }
    },
    "GigabitEthernet0/1": {
        "zone": {
            "name": "outside",
            "security_level": 0
        },
        "ip_address": {
            "ip": "10.1.2.0",
            "mask": 24
        }
    }
}
"""
