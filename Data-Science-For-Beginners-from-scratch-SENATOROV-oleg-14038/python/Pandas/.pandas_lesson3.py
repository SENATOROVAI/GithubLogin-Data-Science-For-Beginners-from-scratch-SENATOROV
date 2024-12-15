# +
"""This module provides utilities for data manipulation and analysis.

It leverages numpy and pandas to perform operations on arrays and data frames,
and includes type annotations for better code clarity.
"""

import numpy as np
import pandas as pd

# Your code here...
# -

obj = pd.Series([1, 2, 3])
obj

# ?obj

obj = pd.Series([1, 2, 3], index=["a", "b", "c"])
obj.array  # [1, 2, 3]

obj.index

obj["a"]

obj["a"] = 1
obj

obj[["a", "b"]]

obj[obj > 1]

obj * 2
"a" in obj  # return bool

data = {"Moscow": 12000000, "SPB": 7000000}
obj3 = pd.Series(data)
obj3

obj3.to_dict()

data_index = ["Oms", "Ekb", "Moscow"]
obj4 = pd.Series(data, index=data_index)
obj4

pd.isna(obj4)  # isna проверка на Null

pd.notna(obj4)

obj3 + obj4

# Имя сириуса
obj4.name = "population"
obj4

# Добавил столбец msk
obj4.index.name = "msk"
obj4

# +
# Создаем данные, преобразуем в список
data_one: dict[str, list[str]] = {
    "Moscow": list(np.arange(1, 4)),  # Преобразование в список
    "SPB": list(np.arange(1, 4)),  # Преобразование в список
}

# Создаем data_oneFrame
df = pd.DataFrame(data_one)

print(df)
# -

df.head(10)  # df.head(n: 'int' = 5) -> 'Self'

df.tail(10)

# +
# Устанавливаем новый индекс
index: list[str] = ["test1", "test2", "test3"]

# Устанавливаем новые имена столбцов
columns = ["City", "City"]

index1 = columns

col = index

print(df.col)

print(df.index1)
# -

df.Moscow

df.loc["test1"]  # loc -> принимает строку (имя индекса)

df.iloc[0]  # принимает число (номер строки)

# +
df["diff"] = "oleg"  # Добавление столбца d
df["diff"] = np.arange(3.0)  # np.arange(0, 3.)

# del df["Moscow"] # удаление столбца
