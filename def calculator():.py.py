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

calculator()