import sqlite3
import pandas as pd

# Table: Students
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | student_id    | int     |
# | student_name  | varchar |
# +---------------+---------+
# student_id is the primary key (column with unique values) for this table.
# Each row of this table contains the ID and the name of one student in the school.

# Table: Subjects
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | subject_name | varchar |
# +--------------+---------+
# subject_name is the primary key (column with unique values) for this table.
# Each row of this table contains the name of one subject in the school.

# Table: Examinations
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | student_id   | int     |
# | subject_name | varchar |
# +--------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each student from the Students table takes every course from the Subjects table.
# Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
 
# Write a solution to find the number of times each student attended each exam.
# Return the result table ordered by student_id and subject_name.

query = """
SELECT S.student_id, S.student_name, SB.subject_name, COUNT(E.student_id) AS attended_exams
FROM Students S 
CROSS JOIN Subjects SB
LEFT JOIN Examinations E ON S.student_id = E.student_id AND SB.subject_name = E.subject_name
GROUP BY S.student_id, S.student_name, SB.subject_name
ORDER BY S.student_id ASC, SB.subject_name ASC;
"""

schema = """
CREATE TABLE IF NOT EXISTS Students (student_id INT, student_name VARCHAR(20));
CREATE TABLE IF NOT EXISTS Subjects (subject_name VARCHAR(20));
CREATE TABLE IF NOT EXISTS Examinations (student_id INT, subject_name VARCHAR(20));

-- Clear all data from the tables
DELETE FROM Students;
DELETE FROM Subjects;
DELETE FROM Examinations;

-- Insert data into Students table
INSERT INTO Students (student_id, student_name) VALUES ('1', 'Alice');
INSERT INTO Students (student_id, student_name) VALUES ('2', 'Bob');
INSERT INTO Students (student_id, student_name) VALUES ('13', 'John');
INSERT INTO Students (student_id, student_name) VALUES ('6', 'Alex');

-- Insert data into Subjects table
INSERT INTO Subjects (subject_name) VALUES ('Math');
INSERT INTO Subjects (subject_name) VALUES ('Physics');
INSERT INTO Subjects (subject_name) VALUES ('Programming');

-- Insert data into Examinations table
INSERT INTO Examinations (student_id, subject_name) VALUES ('1', 'Math');
INSERT INTO Examinations (student_id, subject_name) VALUES ('1', 'Physics');
INSERT INTO Examinations (student_id, subject_name) VALUES ('1', 'Programming');
INSERT INTO Examinations (student_id, subject_name) VALUES ('2', 'Programming');
INSERT INTO Examinations (student_id, subject_name) VALUES ('1', 'Physics');
INSERT INTO Examinations (student_id, subject_name) VALUES ('1', 'Math');
INSERT INTO Examinations (student_id, subject_name) VALUES ('13', 'Math');
INSERT INTO Examinations (student_id, subject_name) VALUES ('13', 'Programming');
INSERT INTO Examinations (student_id, subject_name) VALUES ('13', 'Physics');
INSERT INTO Examinations (student_id, subject_name) VALUES ('2', 'Math');
INSERT INTO Examinations (student_id, subject_name) VALUES ('1', 'Math');
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
