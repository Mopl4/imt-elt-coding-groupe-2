-- Bronze products: ~21 columns
SELECT COUNT(*) FROM information_schema.columns
WHERE table_schema = 'bronze_group2' AND table_name = 'products';

-- Silver dim_products: fewer columns (no _* prefix)
SELECT COUNT(*) FROM information_schema.columns
WHERE table_schema = 'silver_group2' AND table_name = 'dim_products';