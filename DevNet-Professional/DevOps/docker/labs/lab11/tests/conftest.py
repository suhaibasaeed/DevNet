from ..schemas.interface import INTERFACE_SCHEMA
from ..schemas.bgp import BGP_SCHEMA
from ..schemas.policy import POLICY_SCHEMA


DATA_MODELS = {
    "interfaces": INTERFACE_SCHEMA,
    "bgp": BGP_SCHEMA,
    "policies": POLICY_SCHEMA,
}


def pytest_addoption(parser):
    parser.addoption(
        "--schema",
        action="append",
        default=[],
        help="list of schemas to validate config files against",
    )


def pytest_generate_tests(metafunc):
    schemas = metafunc.config.getoption("schema") or DATA_MODELS.keys()
    schema_args = [(model, DATA_MODELS[model]) for model in schemas]
    metafunc.parametrize("model,model_schema", schema_args)
