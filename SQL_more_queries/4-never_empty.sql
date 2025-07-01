-- Script para crear la tabla id_not_null con id con valor por defecto 1

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

