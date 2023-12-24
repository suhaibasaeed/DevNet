from flask import Blueprint

VIEW = Blueprint("view", __name__, url_prefix="/views/inventory", template_folder="templates", static_folder="static")
