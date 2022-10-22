
def add_st(db_st, st_new):
    db_st.update(st_new)


def del_st(db_st, st_name):
    if st_name in db_st:
        del db_st[st_name]
        print(f"Ученик {st_name} успешно удален")
    else:
        print(f"Ученика {st_name} в базе данных нет")


def show_student(db_st, st_name):
    if st_name in db_st:
        lst_value = db_st[st_name]
        print(f"Информация о ученике {st_name}")
        for i in range(0, len(lst_value)):
            if i == 0: str_val = "Класс:"
            if i == 1: str_val = "Статус:"
            if i == 2: str_val = "Дата рождения:"
            if i == 4: str_val = "Примечание:"
            if i == 3:
                lst_adress = lst_value[i]
                print("Адрес: " + ", ".join(lst_adress))
            else:
                print(f"{str_val} {lst_value[i]}")
    else:
        print(f"Ученика {st_name} нет в базе")


def show_all(db_st):
    for key in db_st:
        print(f"Ученик {key}")
        lst_value = db_st[key]
        for i in range(0, len(lst_value)):
            if i == 0: str_val = "Класс:"
            if i == 1: str_val = "Статус:"
            if i == 2: str_val = "Дата рождения:"
            if i == 4: str_val = "Примечание:"
            if i == 3:
                lst_adress = lst_value[i]
                print("Адрес: " + ", ".join(lst_adress))
            else:
                print(f"{str_val} {lst_value[i]}")
        print()

def search_students(db_st, st_val):
    lst_key = []
    for key in db_st:
        lst_value = db_st[key]
        if st_val in lst_value:
            lst_key.append(key)
    if len(lst_key) > 0:
        for i in range(0, len(lst_key)):
            show_student(db_st, lst_key[i])
            print()
    else:
        print("")