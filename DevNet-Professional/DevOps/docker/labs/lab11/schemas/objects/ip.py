from ..properties.ip import IP_PROPERTY, MASK_PROPERTY


IP_OBJECT = {
    "type": "object",
    "properties": {
        "ip": IP_PROPERTY,
        "mask": MASK_PROPERTY,
    },
    "required": ["ip", "mask"],
    "additionalProperties": False,
}
"""
EX:
{
    "ip": "10.1.1.1",
    "mask": 24
}
"""
