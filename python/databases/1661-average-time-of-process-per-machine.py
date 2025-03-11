import sqlite3
import pandas as pd

# 1661. Average Time of Process per Machine

# Table: Activity
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | machine_id     | int     |
# | process_id     | int     |
# | activity_type  | enum    |
# | timestamp      | float   |
# +----------------+---------+
# The table shows the user activities for a factory website.
# (machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
# machine_id is the ID of a machine.
# process_id is the ID of a process running on the machine with ID machine_id.
# activity_type is an ENUM (category) of type ('start', 'end').
# timestamp is a float representing the current time in seconds.
# 'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
# The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
# It is guaranteed that each (machine_id, process_id) pair has a 'start' and 'end' timestamp.
 

# There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

# The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

# The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

# Return the result table in any order.

# The result format is in the following example.

 
query = """
WITH Total_time AS
(SELECT A.machine_id, SUM(B.timestamp - A.timestamp) as total_time, Count(DISTINCT A.process_id) as total_processes
FROM Activity A JOIN Activity B 
ON A.machine_id = B.machine_id 
and A.process_id = B.process_id
WHERE B.activity_type = "end"
AND A.activity_type = "start"
GROUP BY A.machine_id)

SELECT machine_id, round((total_time / total_processes), 3) as processing_time
FROM Total_time
"""

schema = """
-- Create the Activity table if it does not exist
CREATE TABLE IF NOT EXISTS Activity (
    machine_id INT,
    process_id INT,
    activity_type TEXT,
    timestamp FLOAT
);

INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES 
(0, 0, 'start', 0.712),
(0, 0, 'end', 1.52),
(0, 1, 'start', 3.14),
(0, 1, 'end', 4.12),
(1, 0, 'start', 0.55),
(1, 0, 'end', 1.55),
(1, 1, 'start', 0.43),
(1, 1, 'end', 1.42),
(2, 0, 'start', 4.1),
(2, 0, 'end', 4.512),
(2, 1, 'start', 2.5),
(2, 1, 'end', 5);
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