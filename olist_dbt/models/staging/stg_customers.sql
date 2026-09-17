WITH source AS (
    SELECT * FROM {{ source('olist', 'customers') }}
)

SELECT
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state
FROM source