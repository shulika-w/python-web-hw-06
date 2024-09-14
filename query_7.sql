-- Знайти оцінки студентів у окремій групі з певного предмета
SELECT students.name AS student_name, grades.grade, subjects.name AS subject_name, groups.name AS group_name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_id = groups.id
WHERE groups.name = 'Group A'
  AND subjects.name = 'Math';