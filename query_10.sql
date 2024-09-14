-- Список курсів, які певному студенту читає певний викладач
SELECT DISTINCT subjects.name AS subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.name = 'Erica Mooney' 
  AND teachers.name = 'William Hodge';