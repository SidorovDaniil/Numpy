import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series
#    Для создания Series можно использовать
#    – списки Python или массивы NumPy
#    – скалярные значения
#    – словари

s_list  = pd.Series([13, 17, 19, 23, 29], index=list("abcde"))
print(s_list, end="\n\n")

s_dict  = pd.Series({"x": 42, "y": 64, "z": 81})
print(s_dict, end="\n\n")

s_numpy = pd.Series(np.linspace(2, 12, 6))
print(s_numpy, end="\n\n")

s_scalar = pd.Series(3.14, index=["π₁", "π₂", "π₃"])
print(s_scalar, end="\n\n")


# 2. Привести различные способы создания объектов типа DataFrame
#    DataFrame. Способы создания

print("--------------------------")

# – через объекты Series
row_D = pd.Series(["D1", "D2", "D3"], name="row_D")
row_E = pd.Series(["E1", "E2", "E3"], name="row_E")
row_F = pd.Series(["F1", "F2", "F3"], name="row_F")
df_series = pd.DataFrame([row_D, row_E, row_F])
print(df_series, end="\n\n")

# – словари объектов Series
df_dict_of_series = pd.DataFrame({"left": s_list, "right": s_dict})
print(df_dict_of_series, end="\n\n")

# – списки словарей
people = [
    {"name": "Jane",  "age": 26, "job": "analyst"},
    {"name": "Mark",  "age": 41, "job": "pilot"},
    {"name": "Susan", "age": 35, "job": "chef"},
]
df_list_of_dicts = pd.DataFrame(people)
print(df_list_of_dicts, end="\n\n")

# – двумерный массив NumPy
arr2d = np.array([[7,  8,  9],
                  [1,  4, 16],
                  [2, 18, 27]])
df_from_ndarray = pd.DataFrame(arr2d, columns=list("XYZ"))
print(df_from_ndarray, end="\n\n")

# – структурированный массив NumPy
structured = np.array(
    [(501, "Red",   0.12), (502, "Green", 0.34), (503, "Blue", 0.56)],
    dtype=[("code", "i4"), ("label", "U5"), ("prob", "f4")]
)
df_struct = pd.DataFrame(structured)
print(df_struct, end="\n\n")


# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так,
#    чтобы вместо NaN было установлено значение 1

print("--------------------------")
s_left  = pd.Series(np.arange(70, 73),   index=[0, 1, 2])
s_right = pd.Series(np.arange(900, 903), index=[3, 4, 5])
df_merge = pd.DataFrame({"L": s_left, "R": s_right})
print(df_merge.fillna(1), end="\n\n")


# 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ

print('--------------------------')
rng = np.random.default_rng()
A = rng.integers(0,10, (3,4))

df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
print(df)
print(df['a'])
print(df.subtract(df['a'], axis=0))


# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

print("--------------------------")
df_nan = pd.DataFrame(
    [
        [np.nan, 10,     np.nan],
        [5,      np.nan, 15    ],
        [np.nan, np.nan, np.nan],
        [8,      20,     np.nan],
    ],
    columns=["A", "B", "C"],
)
print("Оригинал:\n", df_nan, "\n")

print("ffill():\n", df_nan.ffill(), "\n")   # заполняем вперёд
print("bfill():\n", df_nan.bfill())         # заполняем назад
