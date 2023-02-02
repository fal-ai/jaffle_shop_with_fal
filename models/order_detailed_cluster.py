import pandas as pd
from kmodes.kmodes import KModes

def model(dbt, fal):
    # Look at `fal_project.yml` to see packages installed with this environment
    dbt.config(fal_environment="clustering")

    df: pd.DataFrame = dbt.ref("order_detailed")
    # NOTE: snowflake support
    df.columns = df.columns.str.lower()

    df_train = df[["size", "is_vegan", "is_vegetarian", "is_keto", "shape"]]

    km_2 = KModes(n_clusters=3, init="Huang")
    km_2.fit_predict(df_train)
    df["cluster_label"] = km_2.labels_

    # Hack: postgres adapter doesn't handle dates very well
    df["order_date"] = df["order_date"].astype(str)

    return df
