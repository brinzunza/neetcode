-- Write your query below
SELECT first_name, last_name, city, state
FROM person p
LEFT JOIN address a on p.person_id = a.person_id;