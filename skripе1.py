import re

def passwd():
    while True:
        password = input("Введите пароль: ")
        if len(password) < 6:
            print("Пароль должен содержать не менее 6 символов")
        elif re.search('[0-9]',password) is None:
            print("Пароль должен содержать хотя бы одну цифру ")
        elif re.search("password", password.lower()) is not None: 
            print("Пароль не должен содержать данное слово")
        elif re.search('[a-z]',password.lower()) is None:
            print("Пароль должен содержать хотя бы одну букву ")
        else:
            print("Пароль прошел проверку")
            break

passwd()