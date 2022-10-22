lst_select_menu = []
welcom = "Добро пожаловать в базу данных учеников!"
lst_menu = ["1. Ученик", "2. Поиск", "3. Показать всех", "4. Выход"]
mes_student_menu = "Меню ученик.\nВыберите действие:"
lst_student_menu = ["1. Добавить", "2. Удалить"]
mes_search_menu = "Меню поиск.\nВыберите действие:"
lst_search_menu = ["1. По фамилии", "2. По статусу", "3. По классу"]

def print_menu(lst_menu):
    print("-------------------------------------")
    for i in range(len(lst_menu)):
        print(lst_menu[i])
    print("-------------------------------------")

def ask_menu():
    value = input(">>> ")
    while not (value == "1" or value == "2" or value == "3" or value == "4"):
        print("Неправильный ввод \nОжидалось: 1 или 2 или 3 или 4")
        value = input(">>> ")
    return value

def ask_student_menu(ind):
    lst_select_menu.append(ind)


def ask_search_menu(ind):
    lst_select_menu.append(ind)


def ask_sub_menu(ind):
    lst_select_menu.append(ind)
    if ind == "1":
        print(mes_student_menu)
        print_menu(lst_student_menu)
        value = input(">>> ")
        while not (value == "1" or value == "2"):
            print("Неправильный ввод \nОжидалось: 1 или 2")
            value = input(">>> ")
        ask_student_menu(value) # меню ученик (добавить, удалить, изменить)
    if ind == "2":
        print(mes_search_menu)
        print_menu(lst_search_menu)
        value = input(">>> ")
        while not (value == "1" or value == "2" or value == "3"):
            print("Неправильный ввод \nОжидалось: 1 или 2 или 3")
            value = input(">>> ")
        ask_search_menu(value)
    