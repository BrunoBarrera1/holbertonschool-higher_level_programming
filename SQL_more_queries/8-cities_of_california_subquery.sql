-- Script to list all cities of California using subquery and no JOIN

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;

