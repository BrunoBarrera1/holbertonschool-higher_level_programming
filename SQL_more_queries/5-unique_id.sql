-- Script que crea la tabla unique_id donde 'id' es UNIQUE y tiene valor por defecto 1

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

