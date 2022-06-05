# Write your MySQL query statement below
SELECT
    (select distinct salary 
    from Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1) SecondHighestSalary 
