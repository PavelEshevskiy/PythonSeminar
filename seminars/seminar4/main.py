# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

# Variant 1
# print("Введите любую строку: ", end='')
# text = input()

# list_text = list(text)
# set_text = set(text)
# dict_text = dict()

# for i in set_text:
#     dict_text[i] = 0

# for i in list_text:
#     dict_text[i] = dict_text[i] + 1
#     print(f'{i}_{dict_text[i]}', end=' ')

# Variant 2
# s = 'a a a b c a a d c d d'
# s = s.split()
# print(s)
# final_string = ''
# for i in range(len(s)):
#     if s[0:i].count(s[i]) == 0:
#         final_string += f' {s[i]}'
#     else:
#         final_string += f' {s[i]}_{s[0:i].count(s[i])}'
# print(final_string)

# Variant 3
# string = 'a a a b c a a d d d'


# elements = {}

# mess = ""

# for element in string.split():
#     if element not in elements:
#         elements[element] = 1
#         mess += f"{element} "
#     else:
#         elements[element] += 1
#         mess += f"{element}_{elements[element]-1} "

# print(mess)



# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# Output: 13

# print('aBcdEfg.?,!'.strip('.?,!\n').lower()) для строки

# Variant 1
# print(len(set(input('Введите текст ').upper().replace('.', ' ').split())))

text = '''She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells'''
text = text.lower().strip('.,!?\n').replace('.', ' ').split()

print(len(set(text)))



# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#         max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n)

# Решение
n = int(input())
max_num = 0
while n > 0:
    n = int(input())
    if max_num < n:
        max_num = n
print(max_num)