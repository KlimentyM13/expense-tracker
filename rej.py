class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def info(self):
        print(self.name, " - ", self.amount, "руб.")
expenses = []

while True:
    print("1 - Добавить расход")
    print("2 - Показать все расходы")
    print("3 — Статистика")
    print("4 — Сохранить в файл")
    print("5 — Загрузить из файла")
    print("6 — Выход")
    try:
        x = int(input("Введите номер: "))
        if x == 6:
            break
        elif x == 1:
            a = input("Введите название расхода: ")
            b = int(input("Введите сумму расхода: "))
            e = Expense(a, b)
            expenses.append(e)
        elif x == 2:
            for x in expenses:
                x.info()
        elif x == 3:
            total = 0
            max_amount = 0
            min_amount = 999999
            for x in expenses:
                total += x.amount
                if x.amount > max_amount:
                    max_amount = x.amount
                elif x.amount < min_amount: 
                    min_amount = x.amount
            print("Общая сумма расходов:", total, "руб.")
            print("Максимальный расход:", max_amount)
            print("Минимальный расход:", min_amount)
        elif x == 4:
            with open("expenses.txt", "w") as file:
                for x in expenses:
                    file.write(x.name + " " + str(x.amount) + "\n")
        elif x == 5:
            with open("expenses.txt", "r") as file:
                for line in file.readlines():
                    parts = line.strip().split()
                    e = Expense(parts[0], int(parts[1]))
                    expenses.append(e)
    except ValueError:
        print("Введите число!")