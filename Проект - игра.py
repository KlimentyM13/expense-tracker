import random

pts = 0

while True:
    level = int(input("Выбери уровень сложности (1-3): "))
    if level == 1:
        max_num = 10
        lives = 5
        break
    elif level == 2:
        max_num = 20
        lives = 4
        break
    elif level == 3:
        max_num = 50
        lives = 3
        break
    else:
        print("Такого уровня сложности не существует")

while lives > 0 and pts < 5:
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    v = random.choice(["+", "-", "*"])
    
    if v == "+":
        correct = a + b
        
    elif v == "-":
        correct = a - b
        
    else:
        correct = a * b
        

    print(a, v, b, "= ?")

    try:
        answer = int(input("Введите ответ: "))
        if answer == correct:
            print("Правильно!")
            pts += 1
            print("Твои очки: ", int(pts))
            
        else:
            print("Неправильно!")
            lives -= 1
            print("Твои жизни: ", int(lives))
    except:
        print("Введите число!")
if pts == 5:
    print("Ты выиграл!")
    print("Твои жизни: ", int(lives))

if lives == 0:
    print("Game over")
    print("Твои очки: ", int(pts))