-- Знайти студента із найвищим середнім балом з Biology
SELECT students.name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.name = 'Biology'
GROUP BY students.id, students.name
ORDER BY avg_grade DESC
LIMIT 1;