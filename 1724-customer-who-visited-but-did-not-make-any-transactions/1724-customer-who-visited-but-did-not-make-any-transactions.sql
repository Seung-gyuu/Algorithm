# Write your MySQL query statement below
SELECT customer_id, COUNT(*) as count_no_trans 
FROM visits
LEFT JOIN transactions ON visits.visit_id = transactions.visit_id
WHERE transactions.transaction_id IS NULL
GROUP BY customer_id;

