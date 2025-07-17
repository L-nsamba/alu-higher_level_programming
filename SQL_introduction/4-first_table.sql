-- 4-create_table.sql
-- This script creates a table named 'first_table' with columns 'id' and 'name'.
-- If the table already exists, the script does nothing and does not fail.
-- The database name should be passed as an argument to the mysql command.
-- Usage: cat 4-create_table.sql | mysql -hlocalhost -uroot -p [database_name]

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
