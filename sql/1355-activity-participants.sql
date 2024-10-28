
/*
Find the names of all the activities with neither the maximum nor the minimum number of participants.
Each activity in the Activities table is performed by any person in the table Friends.
Return the result table in any order.

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
| activity      | varchar |
+---------------+---------+

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
*/

WITH count AS (
    SELECT activity, COUNT(id) as user_count
    FROM Friends
    GROUP BY activity
)
SELECT activity
FROM count
WHERE user_count NOT IN (SELECT MIN(user_count) FROM count) AND user_count NOT IN (SELECT MAX(user_count) FROM count)