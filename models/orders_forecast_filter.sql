WITH final AS (

    SELECT
        ds AS order_date,
        yhat_count AS forecast_count,
        trend_count,
        yhat_amount AS forecast_amount,
        trend_amount
    FROM {{ ref('orders_forecast') }}

)

SELECT * FROM final
