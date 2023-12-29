from .properties.policy import INTERFACE_PROPERTY
from .array_properties.policy import POLICY_PROPERTY


POLICY_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "patternProperties": {
        r"^.": {
            "type": "object",
            "properties": {
                "interface": INTERFACE_PROPERTY,
                "policies": POLICY_PROPERTY,
            },
            "required": ["interface", "policies"],
            "additionalProperties": False,
        },
    },
}
"""
EX:
{
    "INSIDE": {
        "interface": "inside",
        "policy": [
            {
                "action": "permit",
                "protocol": "tcp",
                "source": {
                    "ip": "10.1.0.0",
                    "mask": 24
                },
                "destination": {
                    "ip": "10.2.0.0",
                    "mask": 24
                },
                "destination_port": 22
            }
        ]
    }
}
"""
