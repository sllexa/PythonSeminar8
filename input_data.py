
def input_data():
    new_student = {}
    print("Введите фамилию и инициалы (формат: Иванов В.С.):")
    st_name = input(">>> ")
    lst_value = []
    print("Введите класс (формат: 11А):")
    lst_value.append(input(">>> "))
    print("Введите статус (формат: отличник):")
    lst_value.append(input(">>> "))
    print("Введите дату рождения (формат: 10.02.2005):")
    lst_value.append(input(">>> "))
    lst_adress = []
    print("Введите город (формат: Москва):")
    lst_adress.append(input(">>> "))
    print("Введите улицу (формат: пр.Мира):")
    lst_adress.append(input(">>> "))
    print("Введите № дома (формат: 95):")
    lst_adress.append(input(">>> "))
    print("Введите № квартиры (формат: 105):")
    lst_adress.append(input(">>> "))
    lst_value.append(lst_adress)
    print("Введите примечание:")
    lst_value.append(input(">>> "))
    new_student[st_name] = lst_value
    return new_student
