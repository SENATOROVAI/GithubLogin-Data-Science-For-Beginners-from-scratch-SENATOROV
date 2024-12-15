# +
"""Простой модуль для проверки имени пользователя и пароля.

Этот модуль выводит приветствие пользователю по имени и проверяет его пароль.
"""

name = "oleg"
password = "180593"
if name == "oleg":
    print(f"Привет, {name}")
    if password == "18051993":
        print("Доступ разрешен ")
    else:
        print("Неверный пароль ")

# +
# Рассмотрим программу, которая запрашивает ввод имени пользователя и пароля
while True:
    print("Who are you?")
    name3 = input("Введите ИМЯ: ")

    if name3 != "Joe":
        continue  # Инструкция continue, если name не равен 'Joe',
    # то инструкция передается в начало цикла

    print("Hello, Joe. What is the password? (It is a fish)")
    password = input("Введите пароль: ")

    if password == "180593":
        break

print("Access granted.")
