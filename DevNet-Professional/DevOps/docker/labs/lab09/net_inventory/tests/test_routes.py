import json
import pytest
import unittest
import os

from app import create_app
from net_inventory.shared.database import db

DEVICES = [
    {
        "device_type": "switch",
        "hostname": "nyc-rt01",
        "ip_address": "10.201.15.11",
        "os": "ios",
        "password": "Cisco123",
        "role": "dc-spine",
        "site": "nyc",
        "username": "admin",
    },
    {
        "device_type": "switch",
        "hostname": "nyc-rt02",
        "ip_address": "10.201.15.12",
        "os": "ios",
        "password": "Cisco123",
        "role": "dc-spine",
        "site": "nyc",
        "username": "admin",
    },
]


class TestNetInventoryAPI(unittest.TestCase):
    def clean_db(self):
        for device in DEVICES:
            self.app.delete("/api/v1/inventory/devices/{}".format(device["hostname"]), content_type="application/json")

    def test_create_device(self):
        rv = self.app.post(
            "/api/v1/inventory/devices",
            data=json.dumps(
                {
                    "device_type": "switch",
                    "hostname": "nyc-rt03",
                    "ip_address": "10.201.15.14",
                    "os": "ios",
                    "password": "Cisco123",
                    "role": "dc-spine",
                    "site": "nyc",
                    "username": "admin",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(rv.status_code, 201)
        rv = self.app.delete("/api/v1/inventory/devices/nyc-rt03", content_type="application/json")
        self.clean_db()

    def test_get_devices(self):
        rv = self.app.get("/api/v1/inventory/devices", content_type="application/json")
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(len(json.loads(rv.get_data())["data"]), 2)
        self.clean_db()

    def test_get_device(self):
        rv = self.app.get("/api/v1/inventory/devices/{}".format("nyc-rt01"), content_type="application/json")
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(json.loads(rv.get_data())["data"]["ip_address"], "10.201.15.11")
        self.clean_db()

    def setUp(self):

        app = create_app()
        self.app = app.test_client()
        with app.app_context():
            db.reflect()
            db.drop_all()
            db.create_all()
            for device in DEVICES:
                self.app.post("/api/v1/inventory/devices", data=json.dumps(device), content_type="application/json")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
