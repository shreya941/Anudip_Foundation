#LAB1------------------------------------------>

INSERT INTO Student (ID, FirstName, LastName, DateOfBirth, Gender, Email, Phone)
VALUES 
(1, 'Aarav', 'Sharma', '2000-01-15', 'M', 'aarav.sharma@example.com', '9876543210'),
(2, 'Priya', 'Verma', '2001-02-20', 'F', 'priya.verma@example.com', '8765432109'),
(3, 'Rohit', 'Singh', '1999-03-10', 'M', 'rohit.singh@example.com', '7654321098'),
(4, 'Meera', 'Patel', '2002-04-25', 'F', 'meera.patel@example.com', '6543210987'),
(5, 'Vikram', 'Nair', '2001-05-30', 'M', 'vikram.nair@example.com', '5432109876');


INSERT INTO Course (CourseID, CourseTitle, Credits)
VALUES 
(101, 'Mathematics', 4),
(102, 'Physics', 3),
(103, 'Chemistry', 4),
(104, 'Biology', 3),
(105, 'Computer Science', 5);


INSERT INTO Instructor (InstructorID, FirstName, LastName, Email)
VALUES 
(1, 'Rajesh', 'Kumar', 'rajesh.kumar@example.com'),
(2, 'Neha', 'Gupta', 'neha.gupta@example.com'),
(3, 'Amit', 'Chatterjee', 'amit.chatterjee@example.com'),
(4, 'Sunita', 'Desai', 'sunita.desai@example.com'),
(5, 'Manoj', 'Joshi', 'manoj.joshi@example.com');


INSERT INTO Enrollment (EnrollmentID, EnrollmentDate, ID, CourseID, InstructorID)
VALUES 
(1, '2024-01-10', 1, 101, 1),
(2, '2024-01-11', 2, 102, 2),
(3, '2024-01-12', 3, 103, 3),
(4, '2024-01-13', 4, 104, 4),
(5, '2024-01-14', 5, 105, 5);


INSERT INTO Score (ScoreID, CourseID, ID, DateOfExam, CreditObtained)
VALUES 
(1, 101, 1, '2024-03-15', 85),
(2, 102, 2, '2024-03-16', 90),
(3, 103, 3, '2024-03-17', 88),
(4, 104, 4, '2024-03-18', 92),
(5, 105, 5, '2024-03-19', 95);


INSERT INTO Feedback (FeedbackID, ID, Date, InstructorName, Feedback)
VALUES 
(1, 1, '2024-04-01', 'Rajesh Kumar', 'Great course, well taught.'),
(2, 2, '2024-04-02', 'Neha Gupta', 'Very informative and engaging.'),
(3, 3, '2024-04-03', 'Amit Chatterjee', 'Challenging but rewarding.'),
(4, 4, '2024-04-04', 'Sunita Desai', 'Loved the practical examples.'),
(5, 5, '2024-04-05', 'Manoj Joshi', 'Clear and concise teaching.');


#LAB2-------------------------------------------------------------------->

#task1--

UPDATE Student
SET Email = 'Kumar@example.com'
WHERE FirstName = 'Rajesh' AND LastName = 'Kumar';


-- Task 2: Delete student records where last name is Patel
DELETE FROM Student
WHERE LastName = 'Patel';

-- Task 3: List students with first name starting with 'P'
SELECT * FROM Student
WHERE FirstName LIKE 'P%';
