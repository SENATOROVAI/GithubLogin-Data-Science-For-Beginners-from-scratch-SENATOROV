# +
"""Простой модуль, который выводит сообщение "Hello, world.".

пять раз с использованием цикла while.
"""

spam = 0
while spam < 5:
    print("Hello, world.")
    spam = spam + 1

spam = 0
while spam < 5:
    print("Hello, world.")
    spam = spam + 1
# -

name1 = ""
while name1 != "yor name ":
    print("Please type you name ")
    name = input()
print("Thank you ! ")

# Инструкция break
# Существует простой способ заставить программу досрочно выйти из
# цикла while
while True:
    print("Please type your name")
    name = input()
    if name == "your name ":  # Инструкция
        break
print("Thank you")

# Цикл for и функция range()
# Цикл while  выполняется до тех пор, пока условие остается истинным.
print("My name is")
for i in range(5):
    print(i + 1)

total = 0
for num in range(101):
    total = total + num
print(total)

# Эквивалентный цикл while
print("My name is ?")
i = 0
while i < 5:
    print(f"Jimmy Five Times {i}")
    i = i + 1

# Аргументы начала, конца и шага функции range ()
for i in range(12, 16):
    print(i)

# +
# Функция range() очень гибкая в отношении форматирования
# последовательностей целых чисел для циклов for
# Например, можно задать отрицательный шаг, сделать так,
# чтобы отсчет шел от больших значений к меньшим

for i in range(5, -1, -1):
    print(i)
