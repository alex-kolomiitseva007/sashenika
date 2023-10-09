import random
import pymysql.cursors
import pandas as pd
import warnings
import os

import env
import universal

warnings.filterwarnings("ignore")
os.system('cls||clear')
name = input('Имя бд: ')
name_table = input('Имя таблицы: ')
def check_db() -> None:
    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS `%s`" % name)

    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             database=name,
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    print("База данных подключена")

    try:
        cursor.execute("SELECT * FROM %s" % name_table)
    except pymysql.err.MySQLError:
        with open('create_structure.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            cursor.execute(sql_script % name_table)
            conn.commit()
            print("Скрипт SQL успешно выполнен")
    return

def save_result(operation, result):
    conn = pymysql.connect(host='localhost',
                             user=env.USER,
                             password=env.PASSWORD,
                             database=name,
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    stri =  "INSERT INTO " + name_table + f" (operat, result) VALUES (%s, %s)", (operation, str(result))
    print(stri)
    cursor.execute("INSERT INTO " + name_table + f" (operat, result) VALUES (%s, %s)", (operation, str(result)))
    conn.commit()
    return
def save_db_to_xlsx():
    conn = pymysql.connect(host='localhost',
                            user=env.USER,
                            password=env.PASSWORD,
                            database=name,
                            cursorclass=pymysql.cursors.DictCursor)
    new_df = pd.read_sql("SELECT * FROM " + name_table, conn)
    new_df.to_csv("out.txt")
    return

def print_db():
    conn = pymysql.connect(host='localhost',
                            user=env.USER,
                            password=env.PASSWORD,
                            database=name,
                            cursorclass=pymysql.cursors.DictCursor)
    new_df = pd.read_sql("SELECT * FROM " + name_table, conn)
    print(new_df)
    return

def print_exel():
    name = input('Путь до файла и название: ')
    new_df = pd.read_csv(name)
    print(new_df)
    return


def print_odd_numbers():
    A = input('Введите через пробел список чисел: ').split()
    list = [int(i) for i in A ]
    spisok=[]
    for num in list:
        if num % 2 != 0:
            spisok.append(num)
        elif num == 71278:
            break
    print(spisok)
    save_result('Список1: ', spisok)
    return
def gen_spisok():
    A = input('Введите через пробел список чисел: ').split()
    list = [int(i) for i in A if int(i) != 500]
    print(list)
    save_result('Список2: ', list)
    return
def unique_list():
    unique_list = random.sample(range(100), 50)
    print(unique_list)
    save_result('Список3: ', unique_list)
    return


def main():
    run = True
    commands = """==========================================================================
1. Создать таблицу и БД и ввести радиус круга, результат сохранить в MySQL.
2. Выведем нечетные числа из специализированного списка: , результат сохранить в MySQL.
3. Удалить из специализированного списка числа 500:, результат сохранить в MySQL.
4. Сгенерировать уникальный список из 50 элементов, результат сохранить в MySQL.  
5. Все результаты вывести на экран из MySQL.
6. Сохранить все данные из MySQL в Excel.
7. Вывести все данные на экран из Excel.
8. Завершить"""
    while run:
        run = universal.uni(commands,
                      check_db,
                      print_odd_numbers, gen_spisok, unique_list,
                      print_db, save_db_to_xlsx, print_exel)
    return

if __name__ == '__main__':
    main()

