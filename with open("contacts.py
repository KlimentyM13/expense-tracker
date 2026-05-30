students = {}
with open("students.txt", "w") as file:
    file.write("Алекс 75\n")
    file.write("Мария 92\n")
    file.write("Дима 48\n")
    file.write("Катя 88\n")
    file.write("Иван 55\n")
    file.write("Соня 91\n")
best_name = ""
best_score = 0
with open("students.txt", "r") as file:
    for line in file.readlines():
        parts = line.strip().split()
        students[parts[0]] = parts[1]
        print(parts[0], parts[1])
        if int(parts[1]) > best_score:
            best_name = parts[0]
            best_score = int(parts[1])
        if int(parts[1]) < 60:
            print(parts[0], parts[1])
print(best_name, best_score)
