# List
# first_list = [9, 'fkr', True, [1, 2, 3]]

# for i, elemnt in enumerate(first_list):
#     if elemnt == 9:
#         first_list[i] = 'nine'

# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Variant1
n = [int(i) for i in input().split()]
n = set(n)
print(len(n))

# Variant2
a = [1, 1, 2, 0, -1, 3, 4, 4]
b = list(set(a))
print(len(b))

# Variant3
a = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(list(set(a))))

# Variant4

import random

list_1 = list()

for i in range(0, 10):
    n = random.randint(-1, 10)
    list_1.append(n)
print(list_1)
print(set(list_1))
result = len(set(list_1))
print(result)


# Task2
# Variant1
print("Enter num")
num=int(input())
arr.clear()
for i in range(num):
    arr.append(rand.randint(0,10))

print("Enter k")
k=int(input())
print(arr)
arr2=arr[:len(arr)-k]
arr3=arr[len(arr)-k:]
arr3.append(arr2)
print(arr3)

# Variant2
list_1 = []
length = int(input('Enter length of list > '))
k = int(input('k = '))
for i in  range(length):
    list_1.append(int(input()))

print(list_1)

for i in range(k):
    tmp = list_1[-1]
    list_1.insert(0, tmp)
    list_1.pop()

print(list_1)

# Variant3
list = [1, 2, 3, 4, 5]
k = int(input('k = '))

for i in range(k - 1):
    list.insert(0, list.pop())
print(list)

# Variant4
arr = [1, 2, 3, 4, 5]
k = int(input())
for i in range(k):
    elem = arr.pop()
    arr.insert(0, elem)

print(arr)


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


data = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"}
]

unique_values = set()

for item in data:
    for value in item.values():
        unique_values.add(value.strip())  # Добавляем уникальные значения в множество

print(list(unique_values))

# Task4
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]

list = [0,-1,5,2,3]
count = 0
for i in range(len(list) - 1):
    if list[i] < list[i + 1]:
        count+=1
print(count)


# For homework
a=[int(a) for a in input().split() if int(a)>0]
print(a)


list('abcdefg')