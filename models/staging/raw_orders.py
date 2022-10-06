import pandas as pd
import os

def model(dbt, session) -> pd.DataFrame:
    dbt.config(materialized="table")
    url = f"http://{os.environ['JAFFLE_SHOP_HOSTNAME']}/api/orders"
    df = pd.read_json(url, orient="records")
    return df
