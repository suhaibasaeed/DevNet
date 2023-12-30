INTERFACE_PROPERTY = {"type": "string"}

POLICY_ACTION_PROPERTY = {
    "type": "string",
    "enum": ["permit", "deny"],
}

PROTOCOL_PROPERTY = {
    "type": "string",
    "enum": ["ip", "tcp", "udp", "icmp"],
}

PROTOCOL_PORT_PROPERTY = {
    "type": "number",
    "minimum": 1,
    "maximum": 65535,
}
