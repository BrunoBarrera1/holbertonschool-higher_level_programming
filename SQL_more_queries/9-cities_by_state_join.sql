-- Script to list all cities with their state name using JOIN, ordered by cities.id

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

