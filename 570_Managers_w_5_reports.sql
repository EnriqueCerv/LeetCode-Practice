-- # Write your MySQL query statement below
SELECT Manager.name
FROM Employee as Manager
INNER JOIN Employee as Subordinate ON Manager.id = Subordinate.managerId
GROUP BY Manager.id
HAVING COUNT(*) >= 5