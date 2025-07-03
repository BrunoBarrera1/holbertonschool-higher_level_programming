-- Create table unique_id with id INT DEFAULT 1 and UNIQUE constraint on id

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

