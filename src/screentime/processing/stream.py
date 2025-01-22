import polars as pl
from deltalake import DeltaTable
import logging

logger = logging.getLogger(__name__)

def get_last_run(delta_table: DeltaTable) -> str:
    df = pl.read_delta(delta_table)
    last_run = df.select(pl.max("CREATED_AT")).item(0,0)
    if not last_run:
        last_run = "1900-01-01 00:00:00"
    logger.info(f'Last run {last_run}')
    return last_run

def identify_new_records(source_df: pl.DataFrame, last_run: str) -> pl.DataFrame:
    new_records_df = source_df.filter(pl.col("CREATED_AT") > last_run)
    return new_records_df
