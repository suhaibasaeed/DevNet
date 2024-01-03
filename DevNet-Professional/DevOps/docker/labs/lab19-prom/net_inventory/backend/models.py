from sqlalchemy import Column, String
from marshmallow import fields

from sqlalchemy_utils import EncryptedType

from net_inventory.shared.database import DB, MA
from net_inventory.shared.config import get_config

CONFIG = get_config()
KEY = CONFIG["SECRET_KEY"]


class Device(DB.Model):  # pylint: disable=too-few-public-methods

    __tablename__ = "device"

    hostname = Column(String, nullable=False, primary_key=True)
    ip_address = Column(String, nullable=False, unique=True)
    site = Column(String, nullable=False)
    role = Column(String, nullable=False)
    device_type = Column(String, nullable=False)
    os = Column(String, nullable=False)  # pylint: disable=no-member
    username = Column(String, nullable=False)
    password = Column(EncryptedType(String, KEY), nullable=False)

    def __init__(self, hostname, ip_address, site, role, device_type, os, username, password):
        self.hostname = hostname
        self.ip_address = ip_address
        self.site = site
        self.role = role
        self.device_type = device_type
        self.os = os  # pylint: disable=invalid-name
        self.username = username
        self.password = password

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class DeviceSchema(MA.Schema):
    hostname = fields.Str(required=True)
    ip_address = fields.Str(required=True)
    site = fields.Str(required=True)
    role = fields.Str(required=True)
    device_type = fields.Str(required=True)
    os = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
