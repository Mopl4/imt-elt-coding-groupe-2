-- How many tables in your bronze schema?
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'bronze_group2'
ORDER BY table_name;

-- Row counts per table
SELECT 'products' AS table_name, COUNT(*) AS rows FROM bronze_group2.products
UNION ALL
SELECT 'users', COUNT(*) FROM bronze_group2.users
UNION ALL
SELECT 'orders', COUNT(*) FROM bronze_group2.orders
UNION ALL
SELECT 'order_line_items', COUNT(*) FROM bronze_group2.order_line_items
UNION ALL
SELECT 'reviews', COUNT(*) FROM bronze_group2.reviews
UNION ALL
SELECT 'clickstream', COUNT(*) FROM bronze_group2.clickstream;

-- Inspect the columns of the products table — notice the _ prefixed columns
SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'bronze_group2' AND table_name = 'products'
ORDER BY ordinal_position;

-- Quick peek at order statuses
SELECT status, COUNT(*) AS cnt
FROM bronze_group2.orders
GROUP BY status
ORDER BY cnt DESC;

-- Check reviews — what ratings exist?
SELECT rating, COUNT(*) AS cnt
FROM bronze_group2.reviews
GROUP BY rating
ORDER BY rating;

-- Check clickstream — what event types exist   ?
SELECT event_type, COUNT(*) AS cnt
FROM bronze_group2.clickstream
GROUP BY event_type
ORDER BY cnt DESC;