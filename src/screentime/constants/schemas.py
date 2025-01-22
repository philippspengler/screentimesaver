import pyarrow as pa
import polars as pl 

pyarrow_schema = pa.schema([
('TS_START', pa.string()),
("TS_END", pa.string()),
("BUNDLE_ID", pa.string()),
("DURATION_SEC", pa.int64()),
("DURATION_MIN", pa.float64()),
("DEVICE_ID", pa.string()),
("METADATA_NAME", pa.string()),
("METADATA_VALUE", pa.string()),
("DAY_OF_WEEK", pa.string()),
("GMT_OFFSET", pa.int64()),
("CREATED_AT", pa.string()),
("UUID", pa.string()),
("ZMETADATAHASH", pa.string()),
("ZOBJECT_TABLE_ID", pa.string()),
])

polars_schema = {
'TS_START': pl.String(),
"TS_END": pl.String(),
"BUNDLE_ID": pl.String(),
"DURATION_SEC": pl.Int64(),
"DURATION_MIN": pl.Float64(),
"DEVICE_ID": pl.String(),
"METADATA_NAME": pl.String(),
"METADATA_VALUE": pl.String(),
"DAY_OF_WEEK": pl.String(),
"GMT_OFFSET": pl.Int64(),
"CREATED_AT": pl.String(),
"UUID": pl.String(),
"ZMETADATAHASH": pl.String(),
"ZOBJECT_TABLE_ID": pl.String(),
}