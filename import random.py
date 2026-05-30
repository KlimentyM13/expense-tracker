import random

def bilibirda():
    return random.randint(1, 10)

def hui():
    return random.randint(1, 20)

def sho():
    return random.randint(1, 50)

while True:
    lvl = (int(input("Выберите уровень сложности: ")))
    lvl in range (1, 4)
    if lvl == 1:
        lives = 5
        code = bilibirda()
        break
    elif lvl == 2:
        lives = 4
        code = hui()
        break
    elif lvl == 3:
        lives = 3
        code = sho()
        break
    else:
        print("Неправильно выбран уровень сложности")

while lives > 0:
    x = (int(input("Введите число ")))
    if x == code:
        print("Ты угадал")
        break
    
    lives -= 1

    if x < code:
        print("Больше")
        print("Твои жизни: ", int(lives))
    elif x > code:
        print("Меньше")
        print("Твои жизни: ", int(lives))

if lives == 0:
    print("Проиграл")
    print("Твои жизни: ", int(lives), ".")
    print("Правильное число: ", int(code))
    




