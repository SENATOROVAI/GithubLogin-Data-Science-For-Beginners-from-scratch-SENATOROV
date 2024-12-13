# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

"""Example code."""


# Создание вертуального окружение нужно для изоляции одного проекта от другого 

# Подкотовка к созданию окружения 
# # mkdir new_priject 
# # cd new_project 
#

# Создание окружения 
# Python -m venv venv # -m озночает что мы хотим запустить модуль, название модуля venv
# Python3 -m venv 
#
# dir просмотра папок - windows 
# # ls - для Linux 

# venv\venv\activet
#
# source vev/bin/activet - для Linux и Mac 

# Выход 
# deactivate

# pip - package Install Python - система управлния пакетами которая используется для установки и управления программными пакетами 

# Для просмотра установленных   пакетов 
# pip freeze 

# pip  freeze > requerements.txt # Создали фаил с названием пакетов 

# more название фаила для просмотра содержимого 
#

# для установки на новый компютер старых библеотек 
# install -r requerements.txt 

# python для  акивации интепритатора 

# константа это переменная которая не изменяеться в течение всего кода 
#
# MAX_COUNT = 1000
# DAY = 60 * 60 * 24 # количество секунд в сутках 
#

# age = None 

# +
def print_variable_address(a_variable: int) -> None:
    """Print the memory address of the given variable.

    Args:.
        a_variable (int): The variable whose address is to be printed.
    """
    print(id(a_variable))  # Returns the memory address of the object


b_variable: int = 4
print_variable_address(b_variable)
# -

# Ввод и вывод данных 
# print(*object, sep = " ", end = "\n", file =sys.studout, flush=False)

# +
color = input("введите ваш любимый цвет: ")

match color:
    case "Красный" | "Оранжевый":  # | символ или
        print("Любитель красного ")
    case "Зеленный":
        print("Охотник")
    case "черный" | "белый":
        print("скучно")
    case _:  # case _: Равносилен else
        print("Цвета нету ")


# +
def check_value_end(value_one: int) -> None:
    """Check the value and prints a corresponding message.

    Args.
        value_one (int): The integer value to check.
    """
    match value_one:
        case 1:
            print("Значение равно 1")
        case 2:
            print("Значение равно 2")
        case _:
            print("Неизвестное значение")


check_value_end(1)


# -

# def process_data_end(data_input: dict[str, int]) -> None:
#     """Process the provided data and print its type.
#
#     Args:.
#         data_input (dict): The data to process.
#         which can be a tuple, list, or dictionary.
#     """
#     pass
#     match data_input:
#         case (1, 2):
#             print("Data is a tuple (1, 2)")
#         case [1, 2]:
#             print("Data is a list [1, 2]")
#         case dict() if data_input:  # Checks if it's a non-empty dictionary
#             for key, value in data_input.items():
#                 print(f"Data is a dictionary with key '{key}' and value '{value}'")
#         case _:
#             print("Unknown data structure")
#
#
# # Example usage
# data_example = {"oleg": 18}  # Define a dictionary
# process_data_end(data_example)  # Process the dictionary

# Как это работает:
#
#     Кортеж (1, 2): Если данные — кортеж (1, 2), выполнится первый блок.
#     Список [1, 2]: Если данные — список [1, 2], выполнится второй блок.
#     Словарь: Если данные — словарь с ключом key, выполнится третий блок с выводом значения, ассоциированного с этим ключом.
#     Любая другая структура: Если данные не соответствуют ни одному из вышеуказанных шаблонов, будет выполнен блок с _.

# +
def process_number(num_one: int) -> None:
    """Determine if the provided number is positive, negative, or zero.

    Args:.
        num_one (int): The number to be processed.
    """
    match num_one:
        case x if x > 0:
            print(f"{x} — положительное число")
        case x if x < 0:
            print(f"{x} — отрицательное число")
        case _:
            print("Число равно нулю")


num_example = 2

process_number(num_example)
# -

# True and True = True 
#
# False and True = False 
#
# True and False = False 
#
# False and False = False 
#
# True or True = True 
#
# False and True = True
#
# True and False = True 
#
# False and False = False 
#
# True not  True = False
#
# False not  True = True
#
# True and False = True 
#
# False and False = False 

year = int(input("Вв в формате yyyy: "))
if year % 4 != 0:
    print("Обычный")
elif year % 100 == 0 and year % 400 == 0:
    print("Весокосный")
else:
    print("Обычный")

# +
my_math = int(input("2 + 2 = "))
print("Верно" if 2 + 2 == my_math else "Вы уверены")  # Лучще так не надо
# Тернарный оператор

# Если условие if == True мы выводим "Верно"
# Ecли else вы уверены

# +
name = "bob"

if name > "Markus":
    # Cравнение строк проиходит лексекографическом порядке по алфавиту
    print(name)
else:
    print(name)

# +
# Пример 1: Сравнение строк
string1 = "apple"
string2 = "banana"

if string1 < string2:
    print(f'"{string1}" идёт раньше "{string2}" в алфавитном порядке')
else:
    print(f'"{string1}" идёт позже "{string2}" в алфавитном порядке')
# -

# В этом примере строка "apple" идёт раньше, чем строка "banana", поскольку 'a' < 'b' в алфавитном порядке

# Символьное сравнение: При сравнении строк "apple" и "banana" Python начинает сравнение с первого символа. Символ 'a' (из "apple") сравнивается с 'b' (из "banana"). Поскольку 'a' в алфавите идёт раньше 'b', строка "apple" считается меньшей

# Логический цикл while 
# continue - возрашает в начала цикла 
#
# break - досрочная выход из цикла 
#
# действие после else 

# +
num_two = float(input("Введите число: "))

count_one = 0
while count_one < num_two:
    print(count_one)
    count_one += 2  # синтакситечный сахар

# +
num_three = float(input(":>"))

STERP = 2

limitet = num_three - STERP

count_b = -STERP
while count_b < limitet:
    count_b += STERP
    if count_b % 12 == 0:
        continue
    print(count_b)

# +
min_limit = 0
max_limit = 10

while True:
    print("Введите число", min_limit, "и", max_limit, end=" ? 213")
    num_zero = float(input())
    if num_zero < min_limit or num_zero > max_limit:
        print("Неверно")
    else:
        break
print("Было введено число ", num_zero)

# +
min_limit_zero = 0
max_limit_ten = 10
count_a = 3
num: None = None  # Для предотвращение ошибки если coun установят 0 или -1
while count_a > 0:
    print("Попытка", count_a)
    count_a -= 1
    print("Введи число между", min_limit_zero, "и", max_limit_ten, "?")
    num_ren = float(input())
    if num_zero < min_limit_zero or num_ren > max_limit_ten:
        print("Неверно")
    else:
        break
else:
    print("Исчерпаны все попытки")
    exit  # Выход из терминала, в
    # функцию передается число отличие от 0

print("Было введено число ", num)
# -

# Цикл итератор for in 
#
# range по целым числам 
#
# функция enumerate()
#
#

# +
date = [0, 1, 1, 2, 3, 5, 8, 13, 21]

for _ in date:
    print(_)

# +
num_ren = int(input())

for i_num in range(0, num_ren, 2):  # range(stop)
    print(i_num)
# -

count_number = 10
for outer_loop in range(count_number):  # переберет 10
    for middle_loop in range(count_number):  # переберет 100
        for inner_loop in range(count_number):  # Переберет 1000
            print(outer_loop, middle_loop, inner_loop)

# +
animals = ["cat", "dog", "wolf", "rate", "dragon"]

for i_key, animal in enumerate(animals, start=1):  # ключивое слова start = 1
    print(i_key, animal)  # в счечик i передаем 1, слейдуюшие действие 1 + 1
