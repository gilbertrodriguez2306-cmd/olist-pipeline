WITH orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
),

customers AS (
    SELECT * FROM {{ ref('stg_customers') }}
),

payments AS (
    SELECT * FROM {{ ref('stg_order_payments') }}
)

SELECT
    c.customer_city,
    c.customer_state,
    COUNT(o.order_id)        AS total_orders,
    SUM(p.payment_value)     AS total_revenue,
    AVG(p.payment_value)     AS avg_order_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN payments p  ON o.order_id    = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_city, c.customer_state
ORDER BY total_revenue DESC
