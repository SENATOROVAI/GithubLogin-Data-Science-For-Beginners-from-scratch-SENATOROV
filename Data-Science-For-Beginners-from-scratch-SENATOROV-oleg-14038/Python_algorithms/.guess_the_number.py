# +
"""The `import random` allows you to use functions related to.

generating random numbers in your code. `import sys` allows you to interact
with the Python. interpreter and operating system.
"""

import sys

# -

while True:
    print('Введите "exit" для выхода. ')
    response = input()
    if response == "exit":
        sys.exit()
    print("Вы ввели", response, ".")

# +
# sect_number: int = random.randint(
#     1,
#     20,
# )
# # функцию random, randint () для генерации числа, которое должен угадать
# print("Я загадал число от 1 до 20 ")

# for qusses_taken in range(1, 7):  # Игроку дается 6 попыток
#     print("Угадай число ")
#     quests = int(input())

#     if quests < sect_number:
#         print("Число больше ")
#     elif quests > sect_number:
#         print("Число меньше ")
#     else:
#         break  # Число угадал

# if quests == sect_number:
#     print("Отлично,=! Вы угадали.  Количество попыток.")
# else:
#     print("Вы наугада. Я загадал число", (str(quests)), ".")
