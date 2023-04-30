import random
a = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789-_+=!?,."
length = int(input("Скалько символов должен содержать пароль?:  "))
password = "".join(random.sample(a, length))
print(f"Ваш пароль:{password}")