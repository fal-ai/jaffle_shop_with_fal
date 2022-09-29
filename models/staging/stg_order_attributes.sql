with source as (

    select * from {{ ref('raw_order_attributes') }}

)

select * from source
