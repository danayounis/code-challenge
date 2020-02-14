-- Q1:
SELECT class.school,COUNT(students.class_identifier)
FROM students
INNER JOIN class ON students.class_identifier=class.identifier
GROUP BY class.school;

-- Q2:
SELECT class.school,MIN(students.Score),MAX(students.Score),AVG(students.Score)
FROM students
INNER JOIN class ON students.class_identifier=class.identifier
GROUP BY class.school;

-- Q3:
SELECT MIN(students.Score),MAX(students.Score),AVG(students.Score)
FROM students

-- Q4:
SELECT class.school FROM students 
INNER JOIN class ON students.class_identifier=class.identifier
WHERE students.score IN(
SELECT MIN(students.score)
FROM students
);

-- Q5:
SELECT class.school FROM students 
INNER JOIN class ON students.class_identifier=class.identifier
WHERE students.score IN(
SELECT max(students.score)
FROM students
);