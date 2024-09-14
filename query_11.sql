-- Середній бал, який певний викладач ставить певному студентові
SELECT AVG(grades.grade) AS average_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN students ON grades.student_id = students.id
WHERE students.name = 'Erica Mooney' 
  AND teachers.name = 'William Hodge';