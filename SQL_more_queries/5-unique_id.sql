<<<<<<< HEAD
-- Script to create the table 'unique_id' with a unique 'id' and default value 1
=======
-- Script que crea la tabla unique_id donde 'id' es UNIQUE y tiene valor por defecto 1
>>>>>>> f0382271a53fcd72acbab27632922f745edc7f2a

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

