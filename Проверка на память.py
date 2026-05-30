import random

while True:
    try: 
        level = int(input("Выберите уровень (1-3): "))
    except:
        print("Введи число!")
        continue
    
    if level == 1:
        code = random.randint(1, 10)
        lives = 5
        break
    elif level == 2:
        code = random.randint(1, 20)
        lives = 4
        break
    elif level == 3:
        code = random.randint(1, 30)
        lives = 3
        break
    else:
        print("Такого уровня не существует")

while lives > 0:
    try: 
        x = int(input("Введите число: "))
    except:
        print("Введи число!")
        continue

    
    if x == code:
        print("Вы победили!")
        break
    
    lives -= 1

    if x < code:
        print("Больше")
        print("Жизней осталось: ", int(lives))
    elif x > code:
        print("Меньше")
        print("Жизней осталось: ", int(lives))

if lives == 0:
    print("Game Over")
    exit()