import boto3, os
from io import StringIO
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client("s3",
    region_name="eu-west-3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

# --- CSV: Read products.csv ---
response = s3.get_object(Bucket="kickz-empire-data", Key="raw/order_line_items/order_line_items.csv")
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

df = pd.read_csv(StringIO(response["Body"].read().decode("utf-8")))

print(df.shape)        # rows × columns
print(df.dtypes)       # column types
print(df.head())       # first rows
print(df.describe())   # statistics

for col in df.columns:
    print(col)

#question 3
##print(df["status"].unique())

##question 2 :pour les password et ip
#print(df["_hashed_password"].unique())
#print(df["_last_ip"].unique())

#question 4
#bon le 0 ne fonctionne pas surment a cause des arrondit
#print(((df["line_total_usd"] - df["unit_price_usd"] * df["quantity"]).abs() == 0).all())
#version moche
#print(((df["line_total_usd"] - df["unit_price_usd"] * df["quantity"]).abs() < 0.0001).all())


