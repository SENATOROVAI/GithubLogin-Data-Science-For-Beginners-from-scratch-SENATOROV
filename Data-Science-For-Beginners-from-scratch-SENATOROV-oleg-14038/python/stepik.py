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

# https://stepik.org/lesson/375661/step/9?unit=363411
#

"""Модуль для демонстрации работы с уровнями сотрудников и их категориями."""

# +
workers = [
    ["Ivan", "Ivanov", 100000, 2],
    ["Petr", "Petrov", 150000, 2],
    ["Sidor", "Sidorov", 200000, 3],
]

# Перебор списка workers для вывода и анализа уровня сотрудников
for worker in workers:
    name, surname, salary, level = worker
    print(f"Level of {name} {surname}: {level}")

    # Приведение уровня к целому числу
    level = str(level)
    # Обработка уровня сотрудника
    if str(level) > "2":
        print("junior")
    elif str(level) >= "2":
        print("middle")
    else:
        print("senior")
