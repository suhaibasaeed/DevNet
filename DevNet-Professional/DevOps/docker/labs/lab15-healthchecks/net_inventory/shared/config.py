import os
import yaml

# ENV = os.environ.get("ENV", "DEVELOPMENT")
ENV = os.environ.get("ENV")
CONFIG_NAME = "net-inventory-config.yml"


def get_config():
    """
    Returns the path of a config file.
    """
    project_path = os.getcwd()
    config_file = os.path.join(project_path, CONFIG_NAME)
    yaml_config = yaml.load(open(config_file, "r"), Loader=yaml.FullLoader)

    config = yaml_config[ENV]
    # validate_config(config)
    if not config.get("SECRET_KEY"):
        config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    if not config.get("SQLALCHEMY_DATABASE_URI"):
        config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    if not config.get("URL"):
        config["URL"] = os.environ.get("URL", "http://127.0.0.1:5000")

    sql_path = config["SQLALCHEMY_DATABASE_URI"]
    # Work around for slash parsing with sqlite
    if sql_path and sql_path.startswith("sqlite:///") and not sql_path.startswith("sqlite:////"):
        config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + project_path + sql_path[9:]
    return config


class Config:  # pylint: disable=too-few-public-methods
    def __init__(self):
        config = get_config()
        for key, val in config.items():
            setattr(self, key, val)
