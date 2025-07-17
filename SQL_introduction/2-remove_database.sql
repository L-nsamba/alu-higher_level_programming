-- 2-remove_database.sql
-- This script deletes the database 'hbtn_0c_0' from the MySQL server.
-- If the database does not exist, the script does nothing and does not fail.
-- Usage: cat 2-remove_database.sql | mysql -hlocalhost -uroot -p

DROP DATABASE IF EXISTS hbtn_0c_0;
