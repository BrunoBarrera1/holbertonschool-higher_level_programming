-- Lists all records from second_table where name is not NULL or empty, ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
