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

# +
"""
This module provides functionality for working with data using pandas.

It includes functions and utilities to manipulate and analyze data frames.
"""

from typing import List

import pandas as pd

# Your code here...

# +
obj = pd.Series(
    [1, 2, 3], index=["a", "b", "c"], dtype="int8"
)  # int64 принемает  ``-9_223_372_036_854_775_808`` to
# ``9_223_372_036_854_775_807``

# int8 ``-128`` to ``127``
# np.info("int8")
obj.nbytes
# размер объекта, RAM
# obj? # интроспекция, сигнатура функции

obj["a"] = 2
obj[obj < 3]  # filter
# -

obj * 5  # поведение как у вектора
# [1, 2, 3] * 5
"a" in obj

# +
# list1 = ['a','b']
dict_date = {"name": "oleg", "age": 30}
obj_2 = pd.Series(dict_date)

# pd.isna(obj_2) # Чек Nane
obj_2.isna()  # Чек Nane
obj_2 + obj
# -

obj_2.name = "SENATOROV"
obj_2

# +
# DataFrame

data = {"name": ["oleg", "Nefedov"], "age": [30, "May"]}

frame = pd.DataFrame(data)
frame

# +
df = pd.read_csv("https://raw.githubusercontent.")
df_one = "com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"


df_full = df + df_one

# df_full.head()  # show 5 first row
# -

df.tail()  # show 5 end row

df[["survived", "age", "sex"]]
df_on any = df.loc[1]
df["name"] = "SENATOROV"
df_table = df.loc[df.index]
df
df.loc[1]  # вывели 1 index(row) in table

# ### <img src="https://pandas.pydata.org/pandas-docs/stable/_images/03_subset_columns.svg"> -->

# +
# np.info("int8")

# # obj?

help(pd.Series)


# +
def createdataframe(student_data: List[List[int]]) -> pd.DataFrame:
    """Создает DataFrame.

    из списка данных студентов.

    Параметры.

    student_data (List[List[int]]): Список подсписков с идентификатором.
    студента и его возрастом.

    Возвращает.

    pd.DataFrame:DataFrame с данными студентов в столбцах 'student_id' и 'age'.

    """
    column_names = [
        "student_id",
        "age",
    ]  # 3. 'column _ names = [' student _ id ',' age ']':
    # Эта строка создает список под названием 'column _ names'
    # с двумя строками: 'student _ id' и 'age'.
    # Эти строки представляют имена столбцов в результирующем фрейме данны
    result = pd.DataFrame(student_data, columns=column_names)

    return result


# pd.DataFrame(): Это конструктор, предоставляемый
# библиотекой Pandas для создания объекта DataFrame.
# Он используется для создания фрейма данных
# из заданных данных и имен столбцов.

# 2 student_data: Это первый параметр, передаваемый
# конструктору pd.DataFrame().
# Он представляет данные, которые будут использоваться
# для заполнения фрейма данных.
# В данном случае student_data - это список списков,
# где каждый внутренний список представляет собой строку данных.

# 2.1 columns: Это параметр конструктора pd.DataFrame() в Pandas.
# Он используется для указания имен столбцов в создаваемом фрейме данных.

# 2.2 column_names: Это переменная,
# которая содержит список имен столбцов во фрейме данных.
#  Она используется в качестве значения параметра columns.

# 3 Таким образом, код
# result = pd.DataFrame(student_data, columns=column_names)
# создает объект
# Pandas DataFrame с именем result, заполняя его данными из списка
# student_data и используя список
# column_names для указания имен столбцов.
# Результирующий фрейм данных будет содержать
# столбцы студенческого билета и возраста,
# как указано в списке column_names.

# +
def get_dataframe_size(players: pd.DataFrame) -> List[int]:
    """Возвращает размер.

    DataFrame.

    Параметры.

    players (pd.DataFrame): DataFrame с данными игроков.

    Возвращает.

    List[int]: Список, содержащий количество строк и столбцов в DataFrame.
    """
    return [
        players.shape[0],
        players.shape[1],
    ]  # 1. Используя индексацию [0] и [1], извлеките \
    # количество строк и столбцов соответственно:


# Это создает список с количеством строк во фрейме
# данных в качестве первого элемента
# и количеством столбцов в качестве второго элемента.
# Преобразование кортежа фигур непосредственно в список
# Это преобразует кортеж фигур в список, который будет иметь ту же структуру:
# [количество строк, количество столбцов].


# Этот код определяет функцию с именем getDataframeSize, которая принимает
# в качестве параметра объект DataFrame панды, называемый players.
# Функция возвращает список из двух целых чисел: количество строк (ось 0)
# и количество столбцов (ось 1) в DataFrame.

# Атрибут shape в pandas возвращает кортеж, содержащий размеры DataFrame,
# где первый элемент представляет количество строк,
# а второй элемент представляет количество столбцов.

# +
def select_first_rows(employees: pd.DataFrame) -> pd.DataFrame:
    """Возвращает первые три строки DataFrame.

    Параметры.
    employees (pd.DataFrame): DataFrame с данными сотрудников.

    Возвращает.
    pd.DataFrame: DataFrame, содержащий первые три строки исходного DataFrame.
    """
    return employees.head(3)  # `return employees.head(3)` - это операция,
    # которая вызывает метод `head(3)`


# на объекте DataFrame `employees` и возвращает новый
# DataFrame, содержащий первые три строки исходного DataFrame.
