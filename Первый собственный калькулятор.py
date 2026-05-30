x = int(input("Введи 1 число: "))
y = int(input("Введи 2 число: "))
v = input("Выбери знак (+, -, /, *, **): ")

if v == "+":
    result = x + y
    print("Ответ: ", result)

elif v == "-":
    result = x - y
    print("Ответ: ", result)

elif v == "/":
    if y != 0:
        result = x / y
        print("Ответ: ", result)
    else:
        print("На ноль делить нельзя")

elif v == "*":
    result = x * y
    print("Ответ: ", result)

elif v == "**":
    result = x ** y
    print("Ответ: ", result)

else:
    print("Выбран неверный знак")