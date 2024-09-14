-- Знайти які предмети читає певний викладач
SELECT subjects.name AS subject_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.name = 'William Hodge';