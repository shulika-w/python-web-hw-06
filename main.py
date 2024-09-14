import sqlite3
import os
from faker import Faker
import random


dbfile = 'university.db'

def creator():

    fake = Faker()

    # З'єднання з базою даних
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()

    # Створення таблиць
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            group_id INTEGER,
            FOREIGN KEY (group_id) REFERENCES groups (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            grade INTEGER,
            date_received DATE,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (subject_id) REFERENCES subjects (id)
        )
    ''')

    # Заповнення таблиць випадковими даними
    # Додавання груп
    groups = ['Group A', 'Group B', 'Group C']
    for group_name in groups:
        cursor.execute('INSERT INTO groups (name) VALUES (?)', (group_name,))

    # Додавання викладачів
    teachers = [fake.name() for _ in range(5)]
    for teacher_name in teachers:
        cursor.execute('INSERT INTO teachers (name) VALUES (?)', (teacher_name,))

    # Додавання предметів
    subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
    teachers_per_subject = random.sample(teachers, len(subjects))  # Вибираємо унікальний список вчителів

    for i, subject_name in enumerate(subjects):
        teacher_name = teachers_per_subject[i]
        teacher_id = cursor.execute('SELECT id FROM teachers WHERE name = ?', (teacher_name,)).fetchone()[0]
        cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject_name, teacher_id))

    # Додавання студентів
    for _ in range(50):
        student_name = fake.name()
        group_id = random.randint(1, len(groups))
        cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (student_name, group_id))

    # Додавання оцінок
    for student_id in range(1, 51):
        for subject_id in range(1, 6):
            for _ in range(5):
                grade = random.randint(1, 12)
                date_received = fake.date_this_year()
                cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)',
                            (student_id, subject_id, grade, date_received))

    # Збереження змін
    conn.commit()

    # Закриття з'єднання
    conn.close()


def main():

    if dbfile not in os.listdir():
        creator()

    while True:
        script_number = input('Enter script number [1-12]: ')

        if script_number.lower() == 'exit':
            break

        script_filename = f'query_{script_number}.sql'

        try:
            with open(script_filename, 'r', encoding='utf-8') as script_file:
                query = script_file.read()

            lines = query.split('\n')
            descr = next((line for line in lines if line.startswith('--')), None)
            print(descr)

            # З'єднання з базою даних
            conn = sqlite3.connect(dbfile)
            cursor = conn.cursor()
            cursor.execute(query)

            # Отримання результатів та їх виведення
            result = cursor.fetchall()
            for row in result:
                print(row)

        except FileNotFoundError:
            print(f'Script file {script_filename} not found.')
        except sqlite3.Error as e:
            print(f'SQL error: {e}')
        except UnicodeDecodeError as e:
            print(f'Error decoding file: {e}')

        finally:
            # Закриття з'єднання
            conn.close()


if __name__ == '__main__':
    main()