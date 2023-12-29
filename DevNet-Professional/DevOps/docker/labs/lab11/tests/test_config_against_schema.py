import yaml
import jsonschema
import pytest


DEVICES = ["csr1kv1", "csr1kv2", "csr1kv3", "asa1"]


@pytest.mark.parametrize("hostname", DEVICES)
def test_config_definitions_against_schema(hostname, model, model_schema):
    try:
        with open(f"{hostname}/{model}.yml", encoding="UTF-8") as vars_file:
            model_vars = yaml.safe_load(vars_file)
            jsonschema.validate(
                instance=model_vars,
                schema=model_schema,
                format_checker=jsonschema.draft7_format_checker
            )
    except FileNotFoundError:
        pass
