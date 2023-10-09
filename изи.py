import random


def print_odd_numbers(numbers):
    A = input('Введите через пробел список чисел').split()
    list = [int(i) for i in A ]

    spisok=[]
    for num in numbers:
        if num % 2 != 0:
            num.append(spisok)
        elif num == 71278:
            break


def gen_spisok():
    A = input('Введите через пробел список чисел').split()
    list = [int(i) for i in A if int(i) != 500]
    print(list)
    return

numbers = []
while True:
    try:
        num = int(input("Введите число (для завершения введите '-1'): "))
        if num == -1:
            break
        numbers.append(num)
    except ValueError:
        print("Некорректный ввод, попробуйте еще раз.")


print_odd_numbers(numbers)

def unique_list():
    unique_list = random.sample(range(100), 50)
    print(unique_list)
    return


