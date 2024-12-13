# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# <!-- # Оперделить ли введенное число явяляеться простыми
# # Простое число которое делиться на себя или на 1
#  -->
#

# +
"""
Этот скрипт определяет, является ли введенное число простым.

и выводит его делители, если оно непростое.
"""

a_n = int(input("Введите число: "))

k_coun = 0  # Записываем Количество делителей

delit = []

for ran in range(
    1,
    a_n + 1,
):  # Перебераем число от 1 до a + 1 то есть само число включительно
    if a_n % ran == 0:
        k_coun += 1
        delit.append(ran)
if k_coun == 2:  # Если k == 2 то есть у простого числа 2 делителя
    print("Число простое ")
else:
    print("Число непростое ")
    print(delit)  # Выводит все делители числа
# -

# <!-- # Найти сумму цифр введенного числа -->

# +
b_val = int(input("Вв число: "))
summa = 0

while b_val > 0:  # Пока число (a) больше 0
    summa += b_val % 10  # Мы в нашу переменную summa прибавляем
    # последние цифры числа в десятичной системы исчисление
    b_val = (
        b_val // 10
    )  # отрезаем последнию цифру числа в десятичной системой исчесления
print(summa)

# +
# Дан список чисел превратить его в список квадратах этих чисел

List_1 = [4, 5, 6, 7]
list_2 = []

for i_num in List_1:
    list_2.append(i_num**2)
print(list_2)

List_3 = [4, 5, 6]

list_4 = [x_num**2 for x_num in List_3]  # Генератор списков
print(list_4)
# -

# <!-- # Вводиться строка, требуеться удалить из нее повторяющийся символы и все пробелы -->

# +
stroka = input("Введите строку ")
stroka_new = ""

for x_strk in stroka:
    # Если сивола нет в новой  строке
    # (stroka_newe) и этот символ не равен  пробелу
    if x_strk not in stroka_new and x_strk != "":
        stroka_new += x_strk
print(stroka_new)
# -

# <!-- # Вводится строка состаящий из слов разделенными  пробелами, требуется посчитать количествро слов в ней -->
#

s_son = input("Введите строку: ")
k_koleb = 0
for z_zon in s_son:
    if z_zon == " ":
        k_koleb += 1
print(k_koleb + 1)

# <!-- # Найти сумму цифр введенного числа -->

# +
b_vv = int(input("Вв число: "))
summa = 0

while b_vv > 0:  # Пока число (a) больше 0
    summa += b_vv % 10  # Мы в нашу переменную summa прибавляем
    # последние цифры числа в десятичной систему исчисления
    b_vv = b_vv // 10  # отрезаем последнею цифру
    # числа в десятичной системой исчисления
print(summa)

# +
# Дан список чисел превратить его в список квадратах этих чисел

Lists1 = [4, 5, 6, 7]
lists2 = []

for i_va in Lists1:
    lists2.append(i_va**2)
print(lists2)

Lists3 = [4, 5, 6]

lists4 = [x_gen**2 for x_gen in Lists3]  # Генератор списков
print(lists4)

# +
# Вводиться строка, трубиться удалить из н
# ее повторяющийся символы и все пробелы
strok = input("Введите строку ")
strok_newe = ""

for x_no in strok:
    # Если сивола нет в новой  строке
    # (stroka_newe) и этот символ не равен  пробелу
    if x_no not in strok_newe and strok != "":
        strok_newe += x_no
print(strok_newe)

# +
# Вводится строка состаящий из слов разделенными  пробелами,
# требуется посчитать количествро слов в ней
s_sup = input("Введите строку: ")
k_one = 0
for z_zed in s_sup:
    if z_zed == " ":
        k_one += 1
print(k_one + 1)

s2 = input("Введите str: ")
print(len(s2.split()))  # метод split преобразует
# разбивать строку на список

# +
# Ввод даты рождения
date = input("Введите дату рождения в формате ДД.ММ.ГГ: ")

# Разделение строки на день, месяц и год
day_str, month_str, year_str = date.split(".")

# Преобразование строк в целые числа
day = int(day_str)
month = int(month_str)
year = int(year_str)

# Инициализация переменной для хранения суммы цифр
total_sum = 0

# Суммирование цифр дня
while day > 0:
    total_sum += day % 10
    day //= 10

# Суммирование цифр месяца
while month > 0:
    total_sum += month % 10
    month //= 10

# Суммирование цифр года
while year > 0:
    total_sum += year % 10
    year //= 10

# Преобразование суммы в однозначное число
while total_sum >= 10:
    temp_sum = 0
    while total_sum > 0:
        temp_sum += total_sum % 10
        total_sum //= 10
    total_sum = temp_sum

print("Ваше счастливое число:", total_sum)
