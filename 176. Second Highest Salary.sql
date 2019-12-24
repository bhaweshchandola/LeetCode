# Write your MySQL query statement below



select IFNULL((SELECT DISTINCT(Salary) as SecondHighestSalary FROM Employee ORDER BY Salary DESC limit 1,1), null) as SecondHighestSalary;