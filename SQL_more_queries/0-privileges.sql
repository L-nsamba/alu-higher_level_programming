-- Make sure users exist (optional, will error if user exists)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant privileges (optional, for testing)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT ON *.* TO 'user_0d_2'@'localhost';

-- Show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show grants for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
