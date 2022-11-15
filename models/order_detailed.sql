WITH order_attributes AS (

    SELECT *
    FROM {{ ref('stg_order_attributes') }}

), orders_tbl AS (

    SELECT *
    FROM {{ ref('orders') }}

), final AS (

    SELECT *
    FROM order_attributes

    LEFT JOIN orders_tbl
        USING (order_id)

)

SELECT * FROM final
