import json

phone_book = {}
path = 'D:\GB Обучение\Python\PythonSeminars\seminars\seminar9_PhoneBookModuls\phones.json'

def open_file():
    global phone_book
    try:
        with open(path, 'r', encoding = 'UTF-8') as file:
            phone_book = json.load(file)
        return True
    except:
        return False

def save_file():
    try:
        with open(path, 'w', encoding = 'UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii = False, indent = 4)
        return True
    except:
        return False

def check_id():
    if phone_book:
        return max(list(map(int, phone_book))) + 1
    return 1

def add_contact(new: dict[int: dict[str, str]]):
    contact = {check_id(): new}
    phone_book.update(contact)

def search(word: str) -> dict[int: dict[str, str]]:
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result

def change(index: str) -> dict[int: dict[str, str]]:
    for index, contact in phone_book.items():
        if index == contact:
            return contact

# def change(new: dict, index: int | str) -> str:
#         for contact in phone_book:
#             if index == contact.get('id'):
#                 contact['name'] = new.get('name', contact.get('name'))
#                 contact['phone'] = new.get('phone', contact.get('phone'))
#                 contact['comment'] = new.get('comment', contact.get('comment'))
#                 return contact.get('name')

# def change_contact(self, id: str, contact: []) -> dict[int:dict[str, str]]:
#         if id in self.contact:
#             self.contact[id]['name'] = contact[0]
#             self.contact[id]['phone'] = contact[1]
#             self.contact[id]['comment'] = contact[2]
#             return self.contact
#         else:
#             return text.not_id(id)

# def change(index: int, new: dict[str, str]):
#     for key, field in new.items():
#         if field != '':
#             phone_book[index - 1][key] = field
            
def remove(index: str):
    del_cnt = phone_book.pop(index)
    return del_cnt

# def change_contact():
#     show_contact(phone_book)
#     index = int(input('Введите ID контакта, который хотите изменить: '))
#     if index in phone_book:
#         phone_book[index]['name'] = input('Введите новое имя контакта: ')
#         phone_book[index]['phone'] = input('Введите новый номер телефона: ')
#         phone_book[index]['comment'] = input('Введите новый комментарий: ')
#     else:
#         print('Введенный ID не существует!')
#     print('\nКонтакт успешно изменён!')