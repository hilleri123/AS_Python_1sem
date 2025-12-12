with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("input.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line)
        if line.strip() == "":   # если строка пустая
            f.write("\n")        # добавить ещё одну
