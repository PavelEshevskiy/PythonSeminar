# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                         Вывод:
# 7                             3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1                (каждое число вводится с новой строки)

# from random import randint

# n = int(input("Введите длину первого массива: "))
# list_set_1 = [randint(1, 10) for i in range(n)]
# m = int(input("Введите длину второго массива: "))
# list_set_2 = [randint(1, 10) for i in range(m)]
# print(*list_set_1)
# print(*list_set_2)

# set_1 = set(list_set_1)
# set_2 = set(list_set_2)
# set_3 = set_1.difference(set_2)
# print(*set_3)

# variant1

# first_size = int(input('Введите количество элементов первого массива: '))

# print(first_array := [int(input(f'Введите элемент: ')) for _ in range(first_size)])

# second_size = int(input('Введите количество элементов второго массива: '))

# print(second_array := [int(input(f'Введите элемент: ')) for _ in range(second_size)])

# print(result_array := [i for i in first_array if i not in second_array])

# variant2

# import random
# N_1 = int(input("Введите число: "))
# N_2 = int(input("Введите еще одно число: "))
# list_1 = [random.randint(1,15) for a in range(N_1)]
# list_2 = [random.randint(1,15) for y in range(N_2)]
# list_3 = []
# for i in range(len(list_1)):
#     if list_1[i] not in list_2:
#         list_3.append(list_1[i])
# print(f"{list_3} - элементы которых нет во втором массиве")

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:                Ввод:
# 5                    5
# 1 2 3 4 5            1 5 1 5 1
# Вывод:               Вывод:
# 0                    2
# (каждое число вводится с новой строки)

# import random
# list_size = int(input("Введите размер списка: "))
# print(list_1 := [random.randint(0, 10) for i in range(list_size)])
# count = 0
# for i in range(1, len(list_1)-1):
#     if list_1[i-1] < list_1[i] > list_1[i+1]:
#         count += 1
# print(count)

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:                Вывод:
# 1 2 3 2 3            2

# import random
# list_size = int(input("Введите количество элементов массива: "))
# list1 = [random.randint(0, 10) for i in range(list_size)]
# set1 = set(list1)
# count = 0
# for i in set1:
#     count += list1.count(i) // 2
    
# print(list1)
# print(f'Количество парных чисел в массиве: {count}')


# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# Ввод:                       
# 300
# Вывод:
# 220 
# #284

def sum_div(n):
    sum_1 = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sum_1 += i
    return sum_1

empty_dictionary = {}
k = 10000
list_1 = []
for i in range(1, k+1):
    empty_dictionary[i] = sum_div(i)

for j in empty_dictionary:
    if j == empty_dictionary.get(empty_dictionary.get(j)) and j < empty_dictionary.get(j):
        print(j, empty_dictionary.get(j))

# https://t.me/STONE_Py

# https://t.me/dirty_python

# https://www.youtube.com/channel/UCCC7ihYh4SNQZj26adlk2Kg

# https://t.me/dirty_python_bot