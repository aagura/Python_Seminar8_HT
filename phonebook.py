# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
import os


def clear():
    os.system('cls')
    return
    
def show_menu ():
    menu =int(input('Это телефонный справочник.' + '\n'+'\n'
                  +'1-показать справочник,'+ '\n'
                  +'2-найти по фамилии,'+ '\n'
                  +'3-найти по номеру,'+ '\n'
                  +'4-добавить данные, '+ '\n'
                  +'5-сохранить в текстовый файл,'+ '\n'
                  +'6-выход:'+ '\n'+'\n'
                  +'Выберите режим:'))
    clear()
    return menu


def read_csv(file_name):
    data = [] 
    fields = ['Фамилия',"Имя", "Телефон", 'Описание'] 
    with open(file_name, 'r', encoding='utf-8') as fin:
         for line in fin:
            record = dict(zip(fields, line.strip().split(','))) 
            data.append(record)
    return data

def print_result(phone_book):
    # Clearing the Screen
     
    clear()
   
    print('Имя'.ljust(20),'Фамилия'.ljust(20),"Телефон".ljust(20),'Описание'+'\n')
    for item in phone_book:
       print(item['Имя'].ljust(20),item['Фамилия'].ljust(20),item["Телефон"].ljust(20),item['Описание'])
       
   
    print()

# Invoking the command processor and calling the pause command
    os.system('pause')

    clear ()
    return

def find_by_name(phone_book, name):
    for item in phone_book:
        if item["Фамилия"]==name:
            print('Имя'.ljust(20),'Фамилия'.ljust(20),"Телефон".ljust(20),'Описание'+'\n')
            print(item['Имя'].ljust(20),item['Фамилия'].ljust(20),item["Телефон"].ljust(20),item['Описание'])
            print ()
            os.system('pause')

            clear ()
            return 
    print ("Ничего не найдено")
    os.system('pause')

    clear ()
    return 
        
    
def get_search_number():
    number = input('Введите номер для поиска: ')
    return number
    return
def get_search_name():
    name = input('Введите Фамилию для поиска: ')
    return name
def find_by_number(phone_book, number):
    for item in phone_book:
        if item["Телефон"]==number:
            print('Имя'.ljust(20),'Фамилия'.ljust(20),"Телефон".ljust(20),'Описание'+'\n')
            print(item['Имя'].ljust(20),item['Фамилия'].ljust(20),item["Телефон"].ljust(20),item['Описание'])
            print ()
            os.system('pause')

            clear ()
            return 
    print ("Ничего не найдено")
    os.system('pause')

    clear ()
    return
def get_new_user():
    fields = ['Фамилия',"Имя", "Телефон", 'Описание'] 
    list = [input('Введите Фамилию: '),
            input('Введите Имя: '),
            input('Введите Телефон: '),
            input('Введите Описание: ')]
    record = dict(zip(fields, list))
    clear ()
    return record
def add_user(phone_book, user_data):
    if user_data not in phone_book:
        phone_book.append(user_data)
        return
    print ('Пользователь уже существует')
    return
def write_txt(file_name, phone_book):
    with open(file_name, 'w', encoding='utf-8') as fout:
        for i in range (len(phone_book)):
            s=''
            for v in phone_book[i].values(): 
                s += v + ','
            fout.write(f'{s[:-1]}\n')
    print ('Файл сохранен')
    os.system('pause')
    return
def write_csv(file_name,phone_book):
    with open(file_name, 'w', encoding='utf-8') as fout:
        for i in range (len(phone_book)):
            s=''
            for v in phone_book[i].values(): 
                s += v + ','
            fout.write(f'{s[:-1]}\n')
    print ('Файл сохранен')
    os.system('pause')
    return
def  get_file_name ():
    name = input('Введите имя файла: ') +'.txt'
    return name

def work_with_phonebook():
    choice = show_menu()
    phone_book =read_csv('phonebook.csv')
    while (choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            find_by_name(phone_book, name)
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number)) 
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv',phone_book) 
            clear()
        elif choice ==5:
            file_name = get_file_name ()
            write_txt(file_name, phone_book)
            clear ()
        else : print ('некорректный ввод, повторите')
        choice = show_menu()
        
clear()
work_with_phonebook()