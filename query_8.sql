-- Знайти середній бал, який ставить певний викладач
SELECT teachers.name AS teacher_name, AVG(grades.grade) AS average_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
WHERE teachers.name = 'William Hodge'
GROUP BY teachers.id, teachers.name
ORDER BY average_grade DESC;