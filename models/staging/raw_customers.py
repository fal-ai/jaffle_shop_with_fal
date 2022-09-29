import pandas as pd

def model(dbt, session) -> pd.DataFrame:
    dbt.config(materialized="table")
    df = pd.read_csv("http://localhost:5000/customers/data.csv")
    return df
