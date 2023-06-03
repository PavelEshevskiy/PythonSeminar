# Задача 26:  Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B 
# с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

# a = int(input("Введите A: "))
# b = int(input("Введите B: "))

# def exponentiation(a, b): 
#     if b == 0:
#         return 1
#     return a * exponentiation(a, b - 1)

# result = exponentiation(a, b)
# print(f'{a} в степени {b} = {result}')


# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

a = int(input("Введите A: "))
b = int(input("Введите B: "))

def summa(a, b):
    a += 1
    b -= 1
    if b > 0:
        return summa(a, b)
    else:
        return a

result = summa(a, b)
print(f'Результат = {result}')