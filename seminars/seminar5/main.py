# arr - отсоритровнная последовательность. k - число. 
# Нужно найти индекс k. Если k нет, то вывести -1

# Вариант из инета
# Iterative Binary Search Function method Python Implementation 
# It returns index of n in given list1 if present,  
# else returns -1  
# def binary_search(list1, n): 
#     low = 0 
#     high = len(list1) - 1 
#     mid = 0 
 
#     while low  n: 
#             high = mid - 1 
 
#         # If n is smaller, compared to the left of mid 
#         else: 
#             return mid 
 
#             # element was not present in the list, return -1 
#     return -1 
 
 
# # Initial list1 
# list1 = [12, 24, 32, 39, 45, 50, 54] 
# n = 45 
 
# # Function call  
# result = binary_search(list1, n) 
 
# if result != -1: 
#     print("Element is present at index", str(result)) 
# else: 
#     print("Element is not present in list1") 

# Вариант 1
# from random import randint

# a = [randint(1, 50) for i in range(10)]
# a.sort()
# print(a)

# value = int(input("Num: "))
# mid = len(a) // 2
# low = 0
# high = len(a) - 1

# while a[mid] != value and low <= high:
#     if value > a[mid]:
#         low = mid + 1
#     else:
#         high = mid - 1
#     mid = (low + high) // 2

# if low > high:
#     print("-1")
# else:
#     print("index =", mid)

# # Вариант 2

# def search(arr, k):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] < k:
#             low = mid + 1
#         elif arr[mid] > k:
#             high = mid - 1
#         else:
#             return mid

#     return -1

# # Вариант 3

# arr=[1,2,3,4,5,6,7,8,9]
# k=int(input())

# def MyFunc(arr,k):
#     n=len(arr)//2
#     if k>arr[n]:
#        MyFunc(arr[n:],k)
#     elif k<arr[n]:
#         MyFunc(arr[:n],k)
#     else:
#         return n

# print(MyFunc(arr,k))

# # Вариант 4

# n = int(input('Ведите число для указания длины массива: '))
# x = int(input('Укажите искомое число: '))
# list1 = []
# for i in range(n):
#     list1.append(i*2)
# print(list1)


# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         variant = arr[mid]
#         if variant == x:
#             return mid
#         if variant > x:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1


# print(binary_search(list1, x))

# еще вариант
# k=int(input())

# def MyFunc(arr,k):
#     n=len(arr)//2
#     if k>arr[n]:
#        return n+MyFunc(arr[n:],k)
#     elif k<arr[n]:
#         return MyFunc(arr[:n],k)
#     else:
#         return n


# print(MyFunc(arr,k))

# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел 
# a0, a1, ..., an, ..., где a0 = 0, a1  = 1, 
# ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# Вариант 1
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i - 2))
# print(list_1) 

# вариант2

# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         a, b = 0, 1
#         for i in range(2, n+1):
#             c = a + b
#             a, b = b, c
#         return b

# n = int(input("Введите номер числа Фибоначчи: "))
# print("Число Фибоначчи под номером", n, "равно", fib(n))

# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# Вариант 1
# def replace_grades(grades):
#     max_grade = max(grades)
#     min_grade = min(grades)
#     for i in range(len(grades)):
#         if grades[i] == max_grade:
#             grades[i] = min_grade
#         elif grades[i] == min_grade:
#             grades[i] = max_grade
#     return grades

# n = int(input("Введите количество оценок: "))
# grades = list(map(int, input("Введите оценки через пробел: ").split()))
# new_grades = replace_grades(grades)
# print("Новые оценки:", " ".join(map(str, new_grades)))

# вариант 2 не полный

# for i in range(len(list_1)):
#     if list_1[i] == max(list_1):
#         list_1[i] = min(list_1)
# print(list_1)

# Вариант 3

# list1 = [1, 3, 3, 3, 4, 2, 5, 3, 1, 5]
# print(list1)
# max_value = max(list1)
# min_value = min(list1)
# i = 0
# while i < len(list1):
#     if list1[i] == max_value:
#         list1[i] = min_value
#     i += 1
# print(list1)

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# Вариант из инета
# a = int(input("Введите число: "))
# k = 0
# for i in range(2, a // 2+1):
#     if (a % i == 0):
#         k = k+1
# if (k <= 0):
#     print("Число простое")
# else:
#     print("Число не является простым")

# Вариант 1

# def SimpleNum(num):
#     b=True
#     for i in range(2,num):
#         if num%i==0:
#             b=False
#     return b

# print("Enter num")
# n=int(input())
# print(SimpleNum(n))

# вариант 2

# import math

# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(math.sqrt(n))+1, 2):
#             if n % i == 0:
#                 return False
#         return True

# n = int(input("Введите число: "))
# if is_prime(n):
#     print(n, "является простым числом")
# else:
#     print(n, "не является простым числом")

# Вариант 3
# import math

# n = int(input("Введите число: "))

# def prNum(n):
#     for i in range(2, int(math.sqrt(n))):
#         if n % i == 0:
#             return print(f"Число {n} не является простым.")
#     return print(f"Число {n} простое.")

# prNum(n)


# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3