import random 

while True:
    level = int(input("Выбери сложность (1-3): "))
    if level == 1:
        code = random.randint(1, 15)
        lives = 5
        break
    elif level == 2:
        code = random.randint(1, 50)
        lives = 3
        break
    elif level == 3:
        code = random.randint(1, 100)
        lives = 2
        break
    else:
        print("Такого уровня нет")

while lives > 0:
    x = int(input("Введи число: "))
    if x == code:
        break
    elif x > code:
        print("Меньше")
        lives -= 1
        print("Жизней осталось: ", int(lives))
    elif x < code:
        print("Больше")
        lives -= 1
        print("Жизней осталось: ", int(lives))

if lives == 0:
    print("Game Over! Загаданное число было: ", int(code))
else:
    print("Поздравляю, ты выиграл!")
        
    while True:
        print("Хочешь сыграть снова?")
        y = input("Твой ответ (Yes / No): ")
        if y == "Yes":
            print("Хорошо")
            exit()
        elif y == "No":
            print("Окей")
            exit()