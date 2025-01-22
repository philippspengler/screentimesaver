from deltalake import DeltaTable
import deltalake
import os
import polars as pl

def get_or_create_delta_table(path: str, schema: dict):
    if os.path.exists(path) and DeltaTable.is_deltatable(path):
        delta_table = DeltaTable(path)
    else:
        deltalake.DeltaTable.create(path, schema=schema)
        delta_table = DeltaTable(path)
    return delta_table
