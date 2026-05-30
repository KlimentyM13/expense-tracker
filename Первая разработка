import random

def calculator():
    print("\=== КАЛЬКУЛЯТОР ===")
    print("Создатель - Klimentym")

    while True:
        expr = input("Введите пример (или exit): ")

        if expr.lower() == "exit":
            print("Выход")
            break

        try:
            print("Ответ:", eval(expr))
        except:
            print("Ошибка")


Name = input("Введи ник: ")
age = int(input("Введи возраст: "))

if age < 4:
    print("Доступ запрещён")

else:
    while True:
        email = input("Введи почту: ")

        if (
            email.count("@") == 1 and
            "." in email and
            email.index("@") > 0 and
            email.rindex(".") > email.index("@") + 5 and
            not email.endswith(".")
        ):
            print("Почта верная")
            break
        else:
            print("Почта неверная")

    while True:
        password = input("Введи пароль: ")
        check_password = input("Повтори пароль: ")

        if password == check_password and len(password) >= 8:
            print("Пароль верный")
            break
        else:
            print("Ошибка пароля")

    while True:
        code = input("Введи код: ")

        if code.isdigit() and len(code) == 6:
            code = int(code)
            print("Регистрация успешна")
            break
        else:
            print("Неверный код")

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
    print("Ты потерял ", int(5 - lives), " жизней")

if lives == 0:
    print("Game over")
    print("Твои очки: ", int(pts))

print("Проверить все примеры, которые ты решил неправильно можешь здесь:")
calculator()