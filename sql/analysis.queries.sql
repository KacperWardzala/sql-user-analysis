-- Number of sessions per user
SELECT u.user_id, COUNT(s.session_id) AS session_count
FROM users u
LEFT JOIN sessions s ON u.user_id = s.user_id
GROUP BY u.user_id
ORDER BY session_count DESC;

-- Average purchase amount per user
SELECT u.user_id, AVG(p.amount) AS avg_purchase_amount
FROM users u
LEFT JOIN purchases p ON u.user_id = p.user_id
GROUP BY u.user_id
ORDER BY avg_purchase_amount DESC;

-- Total purchases per day
SELECT p.purchase_date, SUM(p.amount) AS total_purchases
FROM purchases p
GROUP BY p.purchase_date
ORDER BY p.purchase_date;
