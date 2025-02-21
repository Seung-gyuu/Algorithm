# Write your MySQL query statement below
-- ROUND( price,2 ) AS average_price
SELECT p.product_id, 
       COALESCE(ROUND(SUM(units * price) / SUM(units), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u 
ON u.purchase_date BETWEEN p.start_date AND p.end_date 
AND p.product_id = u.product_id
GROUP BY p.product_id;