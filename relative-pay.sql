-- A company maintains an EMPLOYEE table with information for each of their employees. Write a query to
-- produce a list containing two columns. The first column should include the name of an employee who
-- earns less than some other employee. The second column should contain the name of a higher earning
-- employee. All combinations of lesser and greater earning employees should be included. Sort
-- ascending, first by the lower earning employee's ID, then by the higher earning employee's SALARY.

SELECT e1.name AS lower_earner, e2.name AS higher_earner
FROM EMPLOYEE e1
INNER JOIN EMPLOYEE e2 ON e1.salary < e2.salary
ORDER BY e1.id ASC, e2.salary ASC;