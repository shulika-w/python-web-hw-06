-- Знайти середній бал у групах з Math
SELECT groups.name AS group_name, subjects.name AS subject_name, AVG(grades.grade) AS average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.name = 'Math' 
GROUP BY groups.id, subjects.id
ORDER BY groups.id, subjects.id;