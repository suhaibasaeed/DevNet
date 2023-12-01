from flask import Flask
from flask_login import LoginManager
from net_inventory.shared.setup import blueprint_by_name, configure_logs, setup_swagger
from net_inventory.shared.database import DB, MA
from net_inventory.shared.config import Config

login_manager = LoginManager()

import jinja2
from flask import request, abort, render_template_string


def register_extensions(app):
    DB.init_app(app)
    MA.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    included_blueprints = app.config["APP"]
    blueprint_by_name(app, included_blueprints)


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        DB.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        DB.session.remove()


def configure_jinja_globals(app):
    @app.context_processor
    def insert_variables():
        return dict(
            render_template_string=render_template_string,
            app_shortname=app.config["APP_SHORTNAME"],
            app_name=app.config["APP_NAME"],
        )

    @jinja2.contextfunction
    def get_context(c):
        return c

    app.jinja_env.globals["context"] = get_context
    app.jinja_env.globals["callable"] = callable


def create_app(selenium=False):
    app = Flask(__name__, static_folder="static")
    config = Config()
    app.config.from_object(config)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if selenium:
        app.config["LOGIN_DISABLED"] = True
    register_extensions(app)
    register_blueprints(app)
    if "net_inventory.backend.api" in app.config["APP"]:
        setup_swagger(app)
        configure_database(app)
    configure_logs(app)
    configure_jinja_globals(app)

    return app
