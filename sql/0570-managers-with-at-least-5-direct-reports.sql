-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | department  | varchar |
-- | managerId   | int     |
-- +-------------+---------+
-- id is the primary key (column with unique values) for this table.
-- Each row of this table indicates the name of an employee, their department, and the id of their manager.
-- If managerId is null, then the employee does not have a manager.
-- No employee will be the manager of themself.
 
-- Write a solution to find managers with at least five direct reports.

-- Return the result table in any order.


WITH count_reports AS (
    SELECT managerId, COUNT(managerId) AS reports
    FROM EMPLOYEE
    WHERE managerID IS NOT NULL
    GROUP BY managerId
)
SELECT E.name
FROM EMPLOYEE E
JOIN count_reports C ON E.id = C.managerId
WHERE C.reports >= 5;