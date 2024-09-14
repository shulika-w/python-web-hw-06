-- Остання Оцінка кожного студента у певній групі з певного предмета
SELECT students.name AS student_name, subjects.name AS subject_name, grades.grade, MAX(grades.date_received) AS last_grade_date
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_id = groups.id
WHERE groups.name = 'Group A'
  AND subjects.name = 'Math'
GROUP BY students.id, students.name, subjects.id
ORDER BY last_grade_date DESC;