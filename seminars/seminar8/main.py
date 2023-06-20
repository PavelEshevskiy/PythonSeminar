# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

phone_book = {}
path: str = 'D:\GB Обучение\Python\PythonSeminars\seminars\seminar8\phones.txt'

def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
    print('\nТелефонная книга успешно загружена!')

def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(data)
    print('\nТелефонная книга успешно сохранена!')
    print('=' * 200 + '\n')

def show_contact(book: dict[int, dict]):
    print('\n' + '=' * 200)
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print('=' * 200 + '\n')

def add_contact():
    uid = max(list(phone_book.keys())) + 1

    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    phone_book[uid] = {'name': name, 'phone': phone, 'comment': comment}

    print(f'\nКонтакт {name} успешно добавлен в книгу!')
    print('=' * 200 + '\n')

def search():
    result = {}
    word = input('Введите слово по которому будет осуществляться поиск: ')
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            result[i] = contact
        else:
            print(f'\nКонтакты со словом {word} не найдены!')
            break
    return result

def change_contact():
    show_contact(phone_book)
    index = int(input('Введите ID контакта, который хотите изменить: '))
    if index in phone_book:
        phone_book[index]['name'] = input('Введите новое имя контакта: ')
        phone_book[index]['phone'] = input('Введите новый номер телефона: ')
        phone_book[index]['comment'] = input('Введите новый комментарий: ')
    else:
        print('Введенный ID не существует!')
    print('\nКонтакт успешно изменён!')


def remove():
    show_contact(phone_book)
    index = int(input('Введите ID контакта, который хотите удалить: '))
    if index in phone_book:
        del_cnt = phone_book.pop(index)
        print(f'\nКонтакт {del_cnt.get("name")} успешно удален из книги!')
        print('=' * 200 + '\n')
    else:
        print('Введенный ID не существует!')

def menu() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
        select = input('Выберете пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Ошибка ввода, введите ЧИСЛО от 1 до 8')

open_file()
while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contact(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            show_contact(result)
        case 6:
            change_contact()
        case 7:
            remove()
        case 8:
            print('До свидания! До новых встреч!')
            break