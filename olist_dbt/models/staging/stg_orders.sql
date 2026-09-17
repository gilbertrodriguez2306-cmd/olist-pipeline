WITH source AS (
    SELECT * FROM {{ source('olist', 'orders') }}
)

SELECT
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp::DATE AS order_purchase_date,
    order_delivered_customer_date::DATE AS order_delivered_date,
    order_estimated_delivery_date::DATE AS order_estimated_delivery_date
FROM source