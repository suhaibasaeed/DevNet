from ..objects.policy import POLICY_OBJECT


POLICY_PROPERTY = {
    "type": "array",
    "items": POLICY_OBJECT,
    "uniqueItems": True,
}
"""
EX:
[
    {
        "action": "permit",
        "protocol": "tcp",
        "source": {
            "ip": "10.1.0.0",
            "mask": 24
        },
        "destination": {
            "ip: "10.2.0.0",
            "mask": 24
        },
        "destination_port": 22
    }
]
"""
