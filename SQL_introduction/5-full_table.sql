-- 5-full_table_description.sql
-- This script prints the full structure of the table 'first_table'
-- from the currently selected database.
-- The database name should be passed as an argument to the mysql command.
-- Usage: cat 5-full_table_description.sql | mysql -hlocalhost -uroot -p [database_name]

SHOW CREATE TABLE first_table;
