class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.done = False
    def info(self):
        print(self.name, "|", self.priority, "|", self.done)
tasks = []

while True:
    print("1 - Добавить задачу")
    print("2 - Показать все задачи")
    print("3 - Выход")
    print("4 — Выполнить задачу")
    print("5 — Статистика")
    try:
        b = int(input("Введите номер: "))
        if b == 1:
            c = input("Название задачи: ")
            d = input("Приоритет?: ")
            t = Task(c, d)
            tasks.append(t)
        elif b == 2:
            for x in tasks:
               x.info() 
        elif b == 3:
            break
        elif b == 4:
            e = input("Название задачи?: ")
            for x in tasks:
                if x.name == e:
                    x.done = True
                    print("Выполнено!")
        elif b == 5:
            done_count = 0
            for x in tasks:
                if x.done == True:
                    done_count += 1
            print("Всего:", len(tasks))
            print("Выполнено:", done_count)
            print("Не выполнено:", len(tasks) - done_count)
    except:
        print("Введите число!")