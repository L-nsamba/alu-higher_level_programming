-- This script lists records from second_table with score >= 10
-- Displays score and name columns (in that order)
-- Orders results by score (highest first)

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
