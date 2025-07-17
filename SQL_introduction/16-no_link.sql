-- This script lists all records from second_table with non-null names
-- Displays score and name columns (in that order)
-- Orders results by score (highest first)
-- Excludes any records where name is NULL

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
