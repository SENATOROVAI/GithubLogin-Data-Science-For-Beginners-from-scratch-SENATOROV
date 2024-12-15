# +
"""Модуль, содержащий типовые аннотации для функций и классов."""


list_name1: list[int] = []
list_name: list[int] = []  # синтаксический сахар

_ = type(list_name), type(list_name1)  # list => name of class


# +
class ListOne:
    """Класс ListOne демонстрирует работу с атрибутами класса и методами."""

    list_number: list[int] = [1, 2, 3]

    def get_value(self, string: str) -> list[int | str]:
        """Возвращает список с числами, строкой и числом 5."""
        return [*self.list_number, string, 5]


# Создание объекта класса ListOne
object_of_class_list1 = ListOne()

# Пример вызова метода get_value
print(object_of_class_list1.get_value("4"))
# Вывод: [1, 2, 3, '4', 5]

# +
list1 = [*range(10)]  # * распаковка => эквивалентно циклу
list1 = []

for item in range(0, 10):
    if item % 2 == 0:
        list1.append(item)

dir(list)
try:
    number = 1
    number += 1
except TypeError:
    print("error")

help(ListOne())

help(ListOne)
