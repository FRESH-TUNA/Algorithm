# Write your MySQL query statement below
SELECT e.name Employee
FROM Employee e
INNER JOIN Employee manager ON e.managerId = manager.id
WHERE e.salary >= manager.salary
