from .ip import IP_OBJECT
from ..properties.policy import (
    POLICY_ACTION_PROPERTY, PROTOCOL_PROPERTY, PROTOCOL_PORT_PROPERTY
)


POLICY_OBJECT = {
    "type": "object",
    "properties": {
        "action": POLICY_ACTION_PROPERTY,
        "protocol": PROTOCOL_PROPERTY,
        "source": IP_OBJECT,
        "destination": IP_OBJECT,
        "destination_port": PROTOCOL_PORT_PROPERTY,
    },
    "required": ["action", "protocol", "source", "destination"],
}
"""
EX:
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
"""
