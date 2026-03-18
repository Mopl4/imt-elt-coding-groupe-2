



from io import BytesIO
import pyarrow.parquet as pq

from io import StringIO
import boto3, os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
s3 = boto3.client("s3",
    region_name="eu-west-3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

# --- Parquet: Read a single partition file ---
response = s3.get_object(
    Bucket="kickz-empire-data",
    Key="raw/clickstream/dt=2026-02-05/part-00001.snappy.parquet"
)
table = pq.read_table(BytesIO(response["Body"].read()))
df_click = table.to_pandas()

print(df_click.shape)
print(df_click.dtypes)
print(df_click.head())

# questions 6
print(df_click["event_type"].unique())