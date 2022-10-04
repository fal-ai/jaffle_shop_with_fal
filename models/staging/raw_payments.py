import pandas as pd
from sshfs import SSHFileSystem


def model(dbt, session) -> pd.DataFrame:
    dbt.config(materialized="table", fal_environment="sftp")

    hostname = "35.193.199.9"

    fs = SSHFileSystem(
        hostname,
        port=2222,
        username="testuser",
        password="testotesto000!!!")

    with fs.open("/data/payments.csv", "r") as f:
        df = pd.read_csv(f)
    return df
