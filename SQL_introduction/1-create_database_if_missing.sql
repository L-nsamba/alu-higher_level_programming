-- 1-create_database_if_missing.sql
-- This script creates the database 'hbtn_0c_0' in the MySQL server.
-- If the database already exists, the script does nothing and does not fail.
-- Usage: cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p

CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
