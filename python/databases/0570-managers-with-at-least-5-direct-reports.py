import sqlite3
import pandas as pd

# -- +-------------+---------+
# -- | Column Name | Type    |
# -- +-------------+---------+
# -- | id          | int     |
# -- | name        | varchar |
# -- | department  | varchar |
# -- | managerId   | int     |
# -- +-------------+---------+
# -- id is the primary key (column with unique values) for this table.
# -- Each row of this table indicates the name of an employee, their department, and the id of their manager.
# -- If managerId is null, then the employee does not have a manager.
# -- No employee will be the manager of themself.
 
# -- Write a solution to find managers with at least five direct reports.

# -- Return the result table in any order.

query = """
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
"""

schema = """
CREATE TABLE If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int);
DELETE FROM Employee;
INSERT INTO Employee (id, name, department, managerId) values ('101', 'John', 'A', NULL);
INSERT INTO Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101');
INSERT INTO Employee (id, name, department, managerId) values ('103', 'James', 'A', '101');
INSERT INTO Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101');
INSERT INTO Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101');
INSERT INTO Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101');
"""

# Set up in-memory SQLite database
conn = sqlite3.connect(':memory:')

# Execute schema and data insertion
conn.executescript(schema)

# Run the query and load results into a DataFrame
result = pd.read_sql_query(query, conn)
print(result)

# Close the connection
conn.close()
