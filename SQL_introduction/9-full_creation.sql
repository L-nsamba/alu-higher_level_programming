-- This script creates a table called second_table if it doesn't exist
-- and inserts multiple records into it

-- Create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert multiple records into the table
-- Using INSERT IGNORE to prevent errors if records already exist
INSERT IGNORE INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
