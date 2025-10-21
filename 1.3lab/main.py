n = int(input("Введите n: "))
x = float(input("Введите x: "))
s = 0

for i in range(n + 1):
    s += ((-1) ** i) * (x ** i)

print("Сумма:", s)
