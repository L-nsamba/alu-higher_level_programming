-- Create user_0d_1 and user_0d_2 if they don't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant root-level privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Create the database user_2_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS user_2_db;

-- Grant only SELECT and INSERT on user_2_db to user_0d_2
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Show privileges for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
