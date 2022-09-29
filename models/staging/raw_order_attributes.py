import pandas as pd

def model(dbt, session) -> pd.DataFrame:
    dbt.config(materialized="table")
    df = pd.read_json("http://localhost:5000/order-attributes", orient="records")
    return df
