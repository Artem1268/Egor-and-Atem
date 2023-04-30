import random
import os
if not os.path.isdir("Passwords"):
    os.mkdir("Passwords")
os.chdir("Passwords")
a = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789-_+=!?,."
length = int(input("Скалько символов должен содержать пароль?:  "))
password = "".join(random.sample(a, length))
print(f"Ваш пароль:{password}")
b = input("Сохронять ли пароль?(Да/Нет)")
с = 0
while c == 0:
    if b == "Да" or "да" or "ДА":
        file = open("passwords.txt")
        file.write(f"{password}\n")
        file.close()
        global c
        c = 1
    elif b == "Нет" or "НЕТ" or "нет":
        global c
        c = 1
    else:
        global b
        b = input("Так да или нет")