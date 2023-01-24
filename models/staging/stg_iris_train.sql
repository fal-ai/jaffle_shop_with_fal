with source as (

    select * from {{ ref('raw_iris_train') }}

)

select * from source
