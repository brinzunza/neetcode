-- Write your query below
SELECT s.seller_name
FROM seller s
WHERE s.seller_id NOT IN (
    SELECT o.seller_id
    FROM orders o
    WHERE o.sale_date <= '2020-12-31' and o.sale_date >= '2020-01-01'
)
ORDER BY seller_name ASC;