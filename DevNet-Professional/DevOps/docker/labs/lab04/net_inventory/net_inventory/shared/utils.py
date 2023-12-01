import inspect
from os.path import dirname, abspath, join

import requests
import yaml

from flask import session, current_app


def api_call(url, method, params=None, json=None):
    if params is None:
        params = {}
    if json is None:
        json = {}
    api_base_url = current_app.config["URL"] + "/api/v1"

    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    try:
        req = getattr(requests, method.lower())(api_base_url + url, params=params, json=json, headers=headers)
    except requests.exceptions.ConnectionError:
        return {"message": "ConnectionError"}

    if req.status_code == 401:
        session.clear()
    return req.json(), req.status_code


def get_parent_root(file):
    return dirname(abspath(file))


def load_yaml(filename):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    caller_dir = dirname(module.__file__)
    file_path = join(caller_dir, filename)
    with open(file_path, "r") as stream:
        data = yaml.load(stream, Loader=yaml.FullLoader)
    return data
