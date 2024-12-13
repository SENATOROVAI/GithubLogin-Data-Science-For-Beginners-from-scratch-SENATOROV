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
Этот модуль загружает данные из CSV-файла и.

обрабатывает их с помощью библиотеки pandas.
"""

import pandas as pd

# +
df_null = pd.read_excel("https://github.com/dm-fedorov/pandas_basic/blob/mas")
df_second = pd.read_excel("ter/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%")

df_third = pd.read_excel(
    "D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas"
)

df_fourth = pd.read_excel("/data/excel-comp-data.xlsx?raw=True")

df_full = pd.read_excel(df_null + df_second + df_third + df_fourth)

df_full
# -

df_full["total"] = df_full["Jan"] + df_full["Feb"] + df_full["Mar"]

df_full.describe()

total_jan = df_full["Jan"].sum()
min_jan = df_full["Jan"].min()
max_jan = df_full["Jan"].max()
mean_jan = df_full["Jan"].mean()

series_data = df_full[["Jan", "Feb", "Mar"]].sum()
series_data

# df_from_series = pd.DataFrame(111, series_data) # позтционные
# df_from_series = pd.DataFrame(data=series_data) # ключеые парамета
df_from_series = pd.DataFrame(
    data=series_data
).T  # T трансопонирование  - заменяет строки на столбцы
df_from_series

df_from_series.T  # изначальный фрейм

print(df_full["Jan"].hist())

# +
df_full.info()

140 160 180

std = 20 # Метрика показ отклонение от среднего 
# -

len(df_full)  # 15 строк

df_full.size, df_full.shape  # 15 строк 10 столбцов

df_full.isnull().sum()  # ноль пустых значений


