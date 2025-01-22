import sqlite3
from os.path import expanduser
import polars as pl
from screentime.utils.delta import get_or_create_delta_table

def load_df_from_query(db_path, query, schema):
    conn = sqlite3.connect(expanduser(db_path))
    df = pl.read_database(
    query=query, 
    connection=conn,
    schema_overrides=schema
    )
    return df
