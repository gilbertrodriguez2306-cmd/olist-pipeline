WITH orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
),

customers AS (
    SELECT * FROM {{ ref('stg_customers') }}
)

SELECT
    c.customer_state,
    COUNT(o.order_id)                                               AS total_orders,
    AVG(
        DATEDIFF('day', o.order_purchase_date, o.order_delivered_date)
    )                                                               AS avg_delivery_days,
    MIN(
        DATEDIFF('day', o.order_purchase_date, o.order_delivered_date)
    )                                                               AS min_delivery_days,
    MAX(
        DATEDIFF('day', o.order_purchase_date, o.order_delivered_date)
    )                                                               AS max_delivery_days
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
  AND o.order_delivered_date IS NOT NULL
GROUP BY c.customer_state
ORDER BY avg_delivery_days ASC