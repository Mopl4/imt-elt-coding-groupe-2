-- Daily revenue
SELECT * FROM gold_group2.daily_revenue ORDER BY order_date LIMIT 5;

-- Top 5 products by revenue
SELECT product_name, brand, total_revenue
FROM gold_group2.product_performance
ORDER BY total_revenue DESC
LIMIT 5;

-- Top 5 customers by spending
SELECT first_name, last_name, loyalty_tier, total_spent, total_orders
FROM gold_group2.customer_ltv
ORDER BY total_spent DESC
LIMIT 5;