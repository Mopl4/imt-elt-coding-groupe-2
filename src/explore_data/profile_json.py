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
# --- JSONL: Read reviews.jsonl ---
response = s3.get_object(Bucket="kickz-empire-data", Key="raw/reviews/reviews.jsonl")
jsonl_content = response["Body"].read().decode("utf-8")

# pd.read_json() with lines=True reads one JSON object per line
df_reviews = pd.read_json(StringIO(jsonl_content), lines=True)

print(df_reviews.shape)
print(df_reviews.dtypes)
print(df_reviews.head())