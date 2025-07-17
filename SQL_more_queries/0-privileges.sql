-- Script to safely show privileges for user_0d_1 and user_0d_2
-- Checks if users exist before attempting to show grants

-- Create temporary procedure to handle privilege display
DELIMITER //
CREATE PROCEDURE ShowUserPrivilegesIfExists(IN username VARCHAR(255))
BEGIN
    DECLARE user_exists INT;

    -- Check if user exists
    SELECT COUNT(*) INTO user_exists FROM mysql.user WHERE user = username AND host = 'localhost';

    -- Show privileges if user exists
    IF user_exists > 0 THEN
        SET @sql = CONCAT("SHOW GRANTS FOR '", username, "'@'localhost'");
        PREPARE stmt FROM @sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    ELSE
        SELECT CONCAT('User ', username, '@localhost does not exist') AS Message;
    END IF;
END //
DELIMITER ;

-- Check privileges for user_0d_1
CALL ShowUserPrivilegesIfExists('user_0d_1');

-- Check privileges for user_0d_2
CALL ShowUserPrivilegesIfExists('user_0d_2');

-- Clean up
DROP PROCEDURE IF EXISTS ShowUserPrivilegesIfExists;
