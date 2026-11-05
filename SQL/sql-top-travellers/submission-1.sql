-- Write your query below
SELECT name, CASE WHEN SUM(distance) IS NULL THEN 0 ELSE SUM(distance) END as travelled_distance
FROM users u
LEFT JOIN rides r ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, name ASC