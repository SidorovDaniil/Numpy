import numpy as np
import array
import sys
import random
# ФИО
# Цифровая кафедра Python
# Дз и конспект по первой лекции
## 1. Какие еще существуют коды типов?
print('Задание 1')
print('''
typecode      Python Type
b               int
B               int
u               Unicode char
w               Unicode char
h               int
H               int
i               int
I               int
l               int
L               int
q               int
Q               int
f               float
d               float
'''
)
## 2. Напишите код, подобный приведенному выше, но с другим типом
print('Задание 2')
a1 = array.array('b', b'abcdef')
print(sys.getsizeof(a1), a1)
print(type(a1))

a2 = array.array('f', [1, 2, 4, 6])
print(a2, type(a2))

## 3. Напишите код для создания массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1

print('Задание 3')
arr = np.linspace(0, 1, 5)
print(arr)

## 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1

print('Задание 4')
arr = np.array([random.random() for i in range(5)])
print(arr)

## 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат.ожиданием = 0 и дисперсией 1

print('Задание 5')
arr = np.random.normal(0, 1, 5)
print(arr)

## 6. Напишите код для создания массива с 5 случайными целыми числами в от [0, 10)

print('Задание 6')
arr = np.array([random.randrange(10) for _ in range(5)])
print(arr)

## 7. Написать код для создания срезов массива 3 на 4

print('Задание 7')
np.random.seed(5)

massive = np.random.randint(10, size = (3, 4))
print(massive)
## - первые две строки и три столбца

print(massive[:2, :3])

## - первые три строки и второй столбец (разве это не то же самое, что и обычный столбец 2?)

print(massive[:, 1:2])

## - все строки и столбцы в обратном порядке

print(massive[::-1, ::-1])

## - второй столбец (вопрос выше)

print(massive[:, 1])

## - третья строка

print(massive[2])

## 8. Продемонстрируйте, как сделать срез-копию

print('Задание 8')

massive = [[2, 3, 4, 5],
           [6, 7, 8, 9],
           [10, 11, 12, 13]]

copy = massive[:]   # срез-копия
# copy = massive.copy()  # другой способ создания копии
print(copy)

copy[0] = 30
print(copy)
print(massive)   #при изменении среза-копии copy, оригинал massive не меняется

print('Задание 9')

vec = np.array([10, 20, 30, 40])
print('Обычный 1-D вектор:\n', vec)

row_vec = vec[np.newaxis, ...]          # эквивалент vec.reshape(1, -1)
print('Вектор-строка (1×4):\n', row_vec)

col_vec = vec[..., np.newaxis]          # эквивалент vec.reshape(-1, 1)
print('Вектор-столбец (4×1):\n', col_vec)


print('\nЗадание 10')

# два одномерных (объём будет 1×N×2)
a = np.array([1, 4, 9, 16])
b = np.array([2, 8, 18, 32])
cube1 = np.dstack((a, b))
print('dstack для 1-D массивов (shape →', cube1.shape, '):\n', cube1)

# два матрицы-столбца (объём будет M×1×2)
left = np.arange(6).reshape(3, 2)        # 3×2
right = np.arange(100, 106).reshape(3, 2)
cube2 = np.dstack((left, right))
print('\ndstack для 2-D массивов (shape →', cube2.shape, '):\n', cube2)

print('\nЗадание 11')

txt = 'Мы все учились понемногу чему-нибудь и как-нибудь'
print('split по пробелу:\n', txt.split())      # обычная строковая split

big = np.arange(24).reshape(6, 4)              # 6×4
print('\nИсходный массив 6×4:\n', big)

print('\nТри вертикальных куска (vsplit):')
for part in np.vsplit(big, 3):
    print(part)

print('\nДва горизонтальных куска (hsplit):')
for part in np.hsplit(big, 2):
    print(part)

cube = big.reshape(3, 2, 4)                    # 3×2×4
print('\nКуб 3×2×4:\n', cube)

print('\nРазбиение вдоль 3-й оси (dsplit на 4 части):')
for slab in np.dsplit(cube, 4):
    print(slab.squeeze())                      # убираем лишнюю ось для компактности

print('\nЗадание 12')

x = np.linspace(-3, 3, 7)          # [-3, …, 3] — удобный диапазон
print('Стартовый x:\n', x)

step1 = np.square(x)               # power(x, 2)
print('Квадрат элемента:\n', step1)

step2 = np.sqrt(step1 + 1)         # ещё одна ufunc
print('sqrt(x² + 1):\n', step2)

step3 = np.exp(step2)              # экспонента
print('exp предыдущего:\n', step3)

step4 = np.log1p(step3)            # ln(1 + x) – безопаснее для мелких x
print('log1p(exp):\n', step4)

step5 = np.floor_divide(step4 * 10, 3)  # floor_divide и multiply одновременно
print('floor_divide((·10), 3):\n', step5)

step6 = np.mod(step5, 5)           # остаток от деления
print('mod (остаток /5):\n', step6)

neg = np.negative(step6)           # унарный минус
print('negative():\n', neg)
