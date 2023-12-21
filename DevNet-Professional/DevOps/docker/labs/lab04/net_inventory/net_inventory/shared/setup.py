import logging
from importlib import import_module
from logging import basicConfig, getLogger, StreamHandler

from flasgger import Swagger


def blueprint_by_name(app, included_blueprints):
    for item in included_blueprints:
        module = import_module(item)
        app.register_blueprint(module.blueprint)


def configure_logs(app):
    basicConfig(
        filename=app.config["LOGGING_LOCATION"],
        level=getattr(logging, app.config["LOGGING_LEVEL"]),
    )
    logger = getLogger()
    logger.addHandler(StreamHandler())


def setup_swagger(app):
    swagger_config = {
        "headers": [],
        "title": "NET INVENTORY",
        "specs": [
            {
                "endpoint": "apispec",
                "route": "/api/spec.json",
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/api/docs/",
    }

    template = {
        "swagger": "2.0",
        "info": {
            "title": "NET INVENTORY",
            "description": "API FOR NET INVENTORY",
            "contact": {
                "responsibleOrganization": "Nexi",
                "responsibleDeveloper": "DevOps Maintainer",
            },
            "version": "1.0",
        },
        "schemes": ["http", "https"],
        "operationId": "getmyData",
    }

    swagger = Swagger(app, config=swagger_config, template=template)
    return swagger
