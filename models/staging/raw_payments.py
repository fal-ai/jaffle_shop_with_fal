import pandas as pd
import os
from sshfs import SSHFileSystem


def model(dbt, session) -> pd.DataFrame:
    dbt.config(materialized="table", fal_environment="sftp")

    hostname = os.environ['JAFFLE_SHOP_HOSTNAME']

    fs = SSHFileSystem(
        hostname,
        port=2222,
        username=os.environ["JAFFLE_SHOP_SSH_USER"],
        password=os.environ["JAFFLE_SHOP_SSH_PASS"])

    with fs.open("/data/payments.csv", "r") as f:
        df = pd.read_csv(f)
    return df
