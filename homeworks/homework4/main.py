# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# from random import randint

# n = int(input("Введите длину первого множества: "))
# list_set_1 = [randint(1, 10) for i in range(n)]
# m = int(input("Введите длину первого множества: "))
# list_set_2 = [randint(1, 10) for i in range(m)]
# print(list_set_1)
# print(list_set_2)

# set_1 = set(sorted(list_set_1))
# set_2 = set(sorted(list_set_2))
# set_3 = set_1.union(set_2)
# print(set_3)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

import random

bush = int(input('Введите количество кустов: '))

list_bush = []
for i in range(bush):
    list_bush.append(random.randint(1, 10))
print(list_bush)

result_count = []
for i in range(bush-1):
    summ = list_bush[i - 1] + list_bush[i] + list_bush[i + 1]
    result_count.append(summ)
result_count.append(list_bush[-2] + list_bush[-1] + list_bush[0])

print(f'Максимальное количество ягод - {max(result_count)}')