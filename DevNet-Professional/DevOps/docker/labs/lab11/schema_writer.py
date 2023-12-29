#!/usr/bin/env python

import argparse
import json
from importlib import import_module


parser = argparse.ArgumentParser(
    description="Writes Schema definition to JSON file"
)
parser.add_argument("schema", type=str, help="Scheme to extrapolate")
args = parser.parse_args()
schema = args.schema

schema_import = f"schemas.{schema}"
schema_name = f"{schema.upper()}_SCHEMA"
schema_module = import_module(schema_import)
schema_definition = getattr(schema_module, schema_name)

with open(f"{schema}_schema.json", mode="w", encoding="utf-8") as fh:
    json.dump(schema_definition, fh, indent=4)
    fh.write("\n")
