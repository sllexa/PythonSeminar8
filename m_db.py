import json

db_students = {}

def load_bd():
    global db_students
    with open('db.json', 'r', encoding='utf-8') as fh:
        db_students = json.load(fh)
    print('БД успешно загружена')


def save_bd():
    with open('db.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(db_students, ensure_ascii=False))
    print('БД успешно сохранена')
