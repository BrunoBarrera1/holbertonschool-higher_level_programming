<<<<<<< HEAD
-- Script to create the database hbtn_0d_usa and table states with constraints
=======
-- Script para crear la base de datos hbtn_0d_usa y la tabla states
>>>>>>> f0382271a53fcd72acbab27632922f745edc7f2a

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

