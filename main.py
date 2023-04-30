from random import choice
playerscore = 0
botscore = 0
while True:
    playerchoice = input("Введите выбор К-камень, Н-ножници, Б-бумага:")
    botchice = choice("КНБ")
    if playerchoice == "К" and botchice == "Н":
        print("Победа!!!")
        playerscore = playerscore + 1
    elif playerchoice == "Н" and botchice == "Б":
        print("Победа!!!")
        playerscore = playerscore + 1
    elif playerchoice == "Б" and botchice == "К":
        print("Победа!!!")
        playerscore = playerscore + 1
    else:
        print("Бот победил")
        botscore = botscore + 1
        print(f"Твой счёт:{playerscore}, Счёт бота:{botscore}")