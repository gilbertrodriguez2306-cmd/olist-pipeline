WITH order_items AS (
    SELECT * FROM {{ ref('stg_order_items') }}
),

payments AS (
    SELECT * FROM {{ ref('stg_order_payments') }}
)

SELECT
    oi.product_id,
    COUNT(oi.order_id)        AS total_orders,
    SUM(oi.price)             AS total_revenue,
    AVG(oi.price)             AS avg_price,
    SUM(oi.total_amount)      AS total_amount_with_freight
FROM order_items oi
JOIN payments p ON oi.order_id = p.order_id
GROUP BY oi.product_id
ORDER BY total_revenue DESC
LIMIT 50