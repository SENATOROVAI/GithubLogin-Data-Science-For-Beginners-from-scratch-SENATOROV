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

# ### Чтобы вызвать метод, нужно создать объект

# +
"""Модуль с импортированными типами для аннотаций."""

from typing import List
# -

my_list: List[int] = []  # в python почти всё объекты
# help(list1) # хелпер, показывает описание объекта
type(my_list)  # показывает называет класса / тип данных
my_list


# +
def get_value(text: str) -> str:  # type hinting / аннотация типов
    """Func def func_name(*arg:rapametr,**kwargs:rapametr)."""
    return f"Hello, {text}"  # f-string, f'', интерполяция


text_word: str = "Word"

dir(get_value)  # показывает атрибуты
get_value(text_word)  # call function

# get_value.__call__(text)
# -

# ### Класс это контейнер для функций

# +
class Oleg:
    """
    Класс для демонстрации работы с.

    атрибутами класса и методами.

    Атрибуты класса.
    - name (str): Имя объекта по умолчанию.

    Методы.
    - set_value(text: str) -> str: Формирует строку.
    с именем объекта и переданным текстом.
    """

    name: str = "Олег"  # переменные это свойство класса / поле класса

    def set_value(self, text: str) -> str:  # функция в классе называется метод
        """
        Формирует строку с именем объекта и текстом.

        который передан в метод.

        Параметры.
        - text (str): Текст.
        который будет включен в результат.

        Возвращает.
        - str: Форматированная строка.
        с именем и текстом.
        """
        return f"{Oleg.name} любит {text}"


obj1 = Oleg()  # создание объекта / экземпляр класса
print(obj1.set_value("математику!"))
# . точечная нотация

obj2 = Oleg()
print(obj2.set_value("программирование!"))
#  вывод строки с другим текстом

# +
x_one = [1, 2, 3]  # список - Структура данных

# алгоритм поиска наибольшего значения
# Алгоритм = последовательность
# действий для выполнения задачи

max_ = x_one[0]  # Создали новую переменную max_ и присвоили
# ей значение элемента с индексом ноль

for num in x_one:  # in оператор членства
    max_ = max(max_, num)  # Используем встроенную
    # функцию max для обновления max_

print(max_)  # Максимальный элемент
