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

# +
"""
Этот модуль загружает данные из CSV-файла.

и обрабатывает их с помощью библиотеки pandas.
"""

import pandas as pd

# +
file_path = "C:/Users/Oleg/Downloads/lesson_1_data (1).csv"

df_r = pd.read_csv(file_path, encoding="windows-1251", sep=";")
df_f = pd.read_csv(file_path, encoding="windows-1251", sep=";")

df_full_name = df_r + df_f

# +
# df.head(3)# выводим первые 3 столбца навой таблицы

# +
# df.tail(1)# выводим последние столбцы

# +
# df.shape # (292, 8) выводим 292 строки 8 колонок

# +
# df.dtypes # выводим типы данных

# +
# f.describe()  # анализирует данные

# +
# df.columns  # Вызывае название калоники
# -

df_ful = df_full_name.rename(
    columns={
        "Номер": "number",
        "Дата создания": "create_date",
        "Дата оплаты": "payment_date",
        "Title": "title",
        "Статус": "status",
        "Заработано": "maney",
        "Город": "city",
        "Платежная система": "payment_system",
    }
)

df_ren = df_full_name.rename(columns={"maney": "money"})
df_ren1 = df_full_name.rename(columns={"Номер": "number"})

all_maney = df_full_name.money.sum()  # Подсчитали общую сумму курсов
all_maney

# +
money_by_city = (
    df_full_name.groupby(["title", "city"], as_index=False)
    .aggregate({"maney": "sum"})
    .sort_values("maney", ascending=False)
)

# df.groupby('title', as_index=False)
# Эта строка группирует фрейм данных df по столбцу 'title'.
#  Функция groupby собирает все строки с одинаковым значением
# в столбце 'title' в отдельные группы.
# Параметр as_index=False гарантирует, что столбец 'title'
# не будет использоваться в качестве индекса в результирующем

# Функция groupby
# собирает все строки с одинаковым значением в столбце 'title'
# в отдельные группы. Параметр as_index=False гарантирует,
# что столбец 'title' не будет использоваться в качестве
# индекса в результирующем фрейме данных.

# aggregate({'mane': 'sum'})

# Эта строка применяет функцию агрегирования к каждой группе,
# вычисляя сумму столбца "many" внутри каждой группы.
# Функция агрегирования используется для указания операции
# агрегирования и столбцов, к которым она должна быть применена.
# В этом случае он агрегирует столбец 'mane', используя функцию 'sum'.

# Функция sort_values
# позволяет вам указать столбец для сортировки
# (в данном случае "many") и в каком порядке следует
# выполнять сортировку: по возрастанию (ascending=True)
# или по убыванию (ascending=False).
# -

all_maney = df_full_name.money.sum()  # Подсчитали общую сумму курсов
all_maney

money = (
    df_full_name.groupby(["title", "city"], as_index=False)
    .aggregate({"money": "sum"})
    .sort_values("money", ascending=False)
)  # сортируем ascending=False
money

money.to_csv("money.csv", index=False)  # Сохраняем фаил

# +
df = pd.read_csv("C:/Users/Oleg/Downloads/lesson")

df_second = pd.read_csv("_1_data (1).csv", encoding="windows-1251", sep=";")

df_full = df + df_second

df_col = df_full.rename(
    columns={
        "Номер": "number",
        "Дата создания": "create_date",
        "Дата оплаты": "payment_date",
        "Title": "title",
        "Статус": "status",
        "Заработано": "money",
        "Город": "city",
        "Платежная система": "payment_system",
    }
)

money_sum = (
    df.query("'status' == 'Завершен'")
    .groupby(["title", "city"], as_index=False)
    .aggregate({"money": "sum", "number": "count"})
    .sort_values("money", ascending=True)
    .rename(columns={"number": "succes_orders"})
)

money_sum.money.sum()
# -

money_sum.money.sum()

money_by_city.to_csv("money_by_city.csv", index=False)

all_maney
