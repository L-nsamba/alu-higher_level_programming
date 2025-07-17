-- This script counts the number of records sharing each score in second_table
-- Results show: score and count of records (labeled as 'number')
-- Sorted by record count (highest first)

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
