import random
import os
if not os.path.isdir("Passwords"):
    os.mkdir("Passwords")
os.chdir("Passwords")
a = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789-_+=!?,."
length = int(input("Скалько символов должен содержать пароль?:  "))
password = "".join(random.sample(a, length))
print(f"Ваш пароль:{password}")
b = input("Сохронять ли пароль?(Да/Нет):  ")
file = open("passwords.txt", "w")
if b == "Да" or "да" or "ДА":
    file.write(f"{password}\n")
else:
    pass
file.close()