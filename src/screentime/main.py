import tomllib
from screentime.processing.io import load_df_from_query
from screentime.queries.appusage import APPUSAGE_SQL
from screentime.processing.stream import get_last_run, identify_new_records
from screentime.utils.delta import get_or_create_delta_table
from screentime.constants.schemas import pyarrow_schema, polars_schema
import argparse
from screentime.utils.logging import setup_logger

def setup_argparse(default_config_path):
    parser = argparse.ArgumentParser(description="Script with config file option.")
    parser.add_argument(
        '--config', 
        type=str, 
        default=default_config_path, 
        help=f'Path to the config file (default: {default_config_path})'
    )
    return parser

def main():
    default_config = "screentimesaver/config/config.toml"
    parser = setup_argparse(default_config_path=default_config)
    args = parser.parse_args()
    logger = setup_logger()

    with open(args.config, "rb") as f:
        config = tomllib.load(f)
    target_delta = get_or_create_delta_table(config["paths"]["delta_table"], pyarrow_schema)
    last_run = get_last_run(target_delta)

    source_df = load_df_from_query(config["paths"]["screentime_db"], APPUSAGE_SQL, polars_schema)

    new_records_df = identify_new_records(source_df, last_run)
    if not new_records_df.is_empty():
        logger.info(f"{len(new_records_df)} new records since last run")
        new_records_df.write_delta(target_delta, mode="append")
    else:
        logger.info('0 new records since last run.')
    
    logger.info('Running vacuum')
    deleted = target_delta.vacuum(dry_run=False)
    logger.info(f'Deleted old files: {deleted}')

if __name__ == "__main__":
    main()


