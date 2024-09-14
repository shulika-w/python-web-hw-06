-- Знайти 5 студентів із найбільшим середнім балом
SELECT students.name AS student_name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.name
ORDER BY average_grade DESC
LIMIT 5;