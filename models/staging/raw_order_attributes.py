import pandas as pd

def model(dbt, session) -> pd.DataFrame:
    dbt.config(materialized="table")
    df = pd.read_json("http://35.196.10.176:8000/order-attributes", orient="records")
    return df
