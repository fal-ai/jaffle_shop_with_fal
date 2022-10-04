import pandas as pd

def model(dbt, session) -> pd.DataFrame:
    dbt.config(materialized="table")
    df = pd.read_json("http://35.193.199.9/api/orders", orient="records")
    return df
