from flask import jsonify, request, abort
from flasgger import swag_from

from net_inventory.backend import API as blueprint
from net_inventory.backend.models import Device, DeviceSchema
from net_inventory.shared.utils import get_parent_root
from net_inventory.shared.database import DB

SWAG_DIR = get_parent_root(__file__) + "/spec/"

DEVICES_SCHEME = DeviceSchema(many=True)


@blueprint.route("/inventory/devices", methods=["GET"])
@swag_from(SWAG_DIR + "get_devices.yml")
def get_devices():
    """
    Update a list of devices

    Returns:
        JSON object
    """
    devices = Device.query.all()
    return jsonify(data=DEVICES_SCHEME.dump(devices)[0]), 200


@blueprint.route("/inventory/devices/<hostname>", methods=["GET"])
@swag_from(SWAG_DIR + "get_device.yml")
def get_device(hostname):
    """
    Get a single device's information

    Path Parameters:
        hostname (str): hostname
    Returns:
        JSON object
    """
    device = Device.query.get_or_404(hostname)
    data, errors = DeviceSchema().dump(device)
    return jsonify(data=data, errors=errors), 200


@blueprint.route("/inventory/devices", methods=["POST"])
@swag_from(SWAG_DIR + "create_device.yml")
def create_device():
    """
    Get a single device's information

    Body Parameters:
        hostname (str): hostname
    Returns:
        JSON object
    """
    DeviceSchema().load(request.json)

    device = Device(**request.json)
    DB.session.add(device)
    DB.session.commit()
    data, errors = DeviceSchema().dump(device)
    return jsonify(data=data, errors=errors), 201


@blueprint.route("/inventory/devices/<hostname>", methods=["PATCH"])
@swag_from(SWAG_DIR + "update_device.yml")
def update_device(hostname):
    """
    Get a single device's information

    Path Parameters:
        hostname (str): hostname
    Returns:
        JSON object
    """
    device = DB.session.query(Device).filter(Device.hostname == hostname).first() # pylint: disable=no-member
    if not device:
        abort(404, {"message": "{} not found".format(hostname)})
    for key, val in request.json.items():
        setattr(device, key, val)
    DB.session.commit()
    data, errors = DeviceSchema().dump(device)
    return jsonify(data=data, errors=errors), 200


@blueprint.route("/inventory/devices/<hostname>", methods=["DELETE"])
@swag_from(SWAG_DIR + "delete_device.yml")
def delete_device(hostname):
    """
    Get a single device's information

    Path Parameters:
        hostname (str): hostname
    Returns:
        JSON object
    """
    device = DB.session.query(Device).filter(Device.hostname == hostname).first() # pylint: disable=no-member
    if not device:
        abort(404, {"message": "{} not found".format(hostname)})
    DB.session.delete(device)
    DB.session.commit()
    return jsonify(), 200
