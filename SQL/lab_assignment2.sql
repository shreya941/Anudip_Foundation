-- Lab 3, ------------------------------------------->

--Task 1: Insert data into Employee table
INSERT INTO Employee (emp_id, first_name, last_name, age, email)
VALUES 
(1, 'Amit', 'Sharma', 28, 'amit.sharma@example.com'),
(2, 'Neha', 'Kapoor', 35, 'neha.kapoor@example.com'),
(3, 'Ravi', 'Singh', 32, 'ravi.singh@example.com'),
(4, 'Meena', 'Desai', 29, 'meena.desai@example.com'),
(5, 'Vikas', 'Nair', 40, 'vikas.nair@example.com');


--Task 2: Retrieve first_name and last_name of all employees
SELECT first_name, last_name FROM Employee;


-- Task 3: Retrieve first_name, last_name, and age of employees older than 30 years
SELECT first_name, last_name, age FROM Employee
WHERE age > 30;


-- Task 4: Increase age of employees by 1 year for all employees older than 25
UPDATE Employee
SET age = age + 1
WHERE age > 25;
