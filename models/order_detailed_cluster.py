"""Cluster orders and upload to data warehouse
Packages:
 - kmodes
"""

import pandas as pd
from kmodes.kmodes import KModes


def model(dbt, session):
    dbt.config(fal_environment="cluster")
    df: pd.DataFrame = dbt.ref("order_detailed")
    df_train = df[["size", "is_vegan", "is_vegetarian", "is_keto", "shape"]]

    km_2 = KModes(n_clusters=3, init="Huang")
    km_2.fit_predict(df_train)
    df["cluster_label"] = km_2.labels_

    # Hack: postgres adapter doesn't handle dates very well
    df['order_date'] = df['order_date'].astype(str)

    return df
