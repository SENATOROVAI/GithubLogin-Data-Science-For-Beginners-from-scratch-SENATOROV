# +
"""Этот модуль выполняет обработку.

данных с использованием библиотеки pandas.
"""

import pandas as pd

# +
df_orig = pd.read_excel("https://raw.githubusercontent.com/")
df_copy = "dm-fedorov/pandas_basic/master/pic/currency_cleanup.png"

df_resalt = df_orig + df_copy

df_resalt
# -

# <img src="https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/pic/currency_cleanup.png">

df_orig["Sales"].astype("float")  # Метод не работает не удаться
# преобразовать строку в число с плавающий точкой

df = df_orig.copy()  # копируем df_orig в df
df

df.info()  # Информация о нашем df

df.dtypes  # Показывает информацию о типах данных

dir(df["Sales"])  # Выводим методы

# +
df["Sales"] = df["Sales"].str.replace(",", "")
df["Sales"] = df["Sales"].str.replace("$", "")

df["Sales"]

# +
df = df_orig.copy()

# Применение функции type к каждому элементу столбца "Sales"
df["Sales_Type"] = df["Sales"].apply(lambda x: type(x).__name__)

print(df)

# +
df["Sales_Type"] = df["Sales"].apply(lambda x: type(x).__name__)

df
# -

type_series = df["Sales"].apply(
    lambda x: str(type(x)),
)  # Показывает количество типов данных
