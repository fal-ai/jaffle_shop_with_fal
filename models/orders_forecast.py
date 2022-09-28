"""Forecast and upload order data
Packages:
 - prophet
"""

import pandas as pd
from prophet import Prophet


def make_forecast(dataframe: pd.DataFrame, periods: int = 30):
    """Make forecast on metric data."""
    model = Prophet(daily_seasonality=False, yearly_seasonality=False)
    model.fit(dataframe)

    future = model.make_future_dataframe(periods=periods)
    prediction = model.predict(future)

    return model, prediction


def model(dbt, fal):
    df: pd.DataFrame = dbt.ref("orders_daily")

    df.columns = df.columns.str.upper()  # Capitalize to make sure Snowflake works
    df_count = df[["ORDER_DATE", "ORDER_COUNT"]]
    df_count = df_count.rename(columns={"ORDER_DATE": "ds", "ORDER_COUNT": "y"})
    model_count, forecast_count = make_forecast(df_count, 50)

    df_amount = df[["ORDER_DATE", "ORDER_AMOUNT"]]
    df_amount = df_amount.rename(columns={"ORDER_DATE": "ds", "ORDER_AMOUNT": "y"})
    model_amount, forecast_amount = make_forecast(df_amount, 50)

    joined_forecast = forecast_count.join(
        forecast_amount.set_index("ds"),
        on="ds",
        lsuffix="_COUNT",
        rsuffix="_AMOUNT",
    )

    # HACK: have to figure out how to write dates (or datetimes) to the database
    # TODO: The types.DATE did not work when testing for `dtype={"ds": types.DATE}`
    joined_forecast["ds"] = joined_forecast["ds"].map(lambda x: x.strftime("%Y-%m-%d"))

    return joined_forecast
