# +
"""The code snippet is a Python program that prompts the user.

for their name and a password. Here's a breakdown of what it does:.'
"""

while True:
    print("Who are you ?")
    name3 = input("Введите ИМЯ")
    if name3 != "Joe":
        continue  # Инструкция continue если name if name не равен
        # Joe' то инструкция передаеться в начала цикла
    print("Helli,Joe. What is the password ? (It is a fish)")
    password = input("Введиете пароль")
    if password == "18.05.93":
        break
print("Access granted. ")
