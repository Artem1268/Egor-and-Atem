import random
playerchoice = input("Введите выбор К-камень, Н-ножници, Б-бумага:")
botchice = random.choice("КНБ")
if playerchoice == "К" and botchice == "Н":
    print("Победа!!!")
elif playerchoice == "Н" and botchice == "Б":
    print("Победа!!!")
elif playerchoice == "Б" and botchice == "К":
    print("Победа!!!")
else:
    print("Бот победил")