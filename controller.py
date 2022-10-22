import console_ui as ui
from input_data import input_data
import students as st
import m_db as db

def start():
    db.load_bd()
    print(ui.welcom)
    while True:
        ui.lst_select_menu.clear()
        ui.print_menu(ui.lst_menu)
        ui.ask_sub_menu(ui.ask_menu())
        if ui.lst_select_menu[0] == "1":
            if ui.lst_select_menu[1] == "1":
                st_new = input_data()
                st.add_st(db.db_students, st_new)
            if ui.lst_select_menu[1] == "2":
                print("Введите фамилию ученика:")
                st_name = input(">>> ")
                st.del_st(db.db_students, st_name)
            if ui.lst_select_menu[1] == "3":
                print("Пока не работает")
        if ui.lst_select_menu[0] == "2":
            if ui.lst_select_menu[1] == "1":
                print("Введите фамилию ученика:")
                st_name = input(">>> ")
                st.show_student(db.db_students, st_name)
            if ui.lst_select_menu[1] == "2":
                print("Введите статус ученика:")
                st_status = input(">>> ")
                st.search_students(db.db_students, st_status)
            if ui.lst_select_menu[1] == "3":
                print("Введите класс ученика:")
                st_class = input(">>> ")
                st.search_students(db.db_students, st_class)
        if ui.lst_select_menu[0] == "3":
            st.show_all(db.db_students)
        if ui.lst_select_menu[0] == "4":
            db.save_bd()
            exit()

