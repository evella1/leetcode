import sqlite3
import pandas as pd

# Find the names of all the activities with neither the maximum nor the minimum number of participants.
# Each activity in the Activities table is performed by any person in the table Friends.
# Return the result table in any order.

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# | activity      | varchar |
# +---------------+---------+

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+


query = """WITH count AS (
    SELECT activity, COUNT(id) as user_count
    FROM Friends
    GROUP BY activity
)
SELECT activity
FROM count
WHERE user_count NOT IN (SELECT MIN(user_count) FROM count) AND user_count NOT IN (SELECT MAX(user_count) FROM count);
"""

schema = """
CREATE TABLE If Not Exists Friends (id int, name varchar(30), activity varchar(30));
CREATE TABLE If Not Exists Activities (id int, name varchar(30));
DELETE FROM Friends;
INSERT INTO Friends (id, name, activity) values ('1', 'Jonathan D.', 'Eating');
INSERT INTO Friends (id, name, activity) values ('2', 'Jade W.', 'Singing');
INSERT INTO Friends (id, name, activity) values ('3', 'Victor J.', 'Singing');
INSERT INTO Friends (id, name, activity) values ('4', 'Elvis Q.', 'Eating');
INSERT INTO Friends (id, name, activity) values ('5', 'Daniel A.', 'Eating');
INSERT INTO Friends (id, name, activity) values ('6', 'Bob B.', 'Horse Riding');
DELETE FROM Activities;
INSERT INTO Activities (id, name) values ('1', 'Eating');
INSERT INTO Activities (id, name) values ('2', 'Singing');
INSERT INTO Activities (id, name) values ('3', 'Horse Riding');
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
