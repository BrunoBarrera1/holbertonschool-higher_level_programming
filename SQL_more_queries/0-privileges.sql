-- Script that shows the privileges of MySQL users user_0d_1 and user_0d_2
-- It assumes both users might or might not exist
-- All SQL keywords are written in UPPERCASE

-- Show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show grants for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
