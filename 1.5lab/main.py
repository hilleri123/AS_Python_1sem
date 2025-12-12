# Вводим и сразу превращаем в числа
spisok = [int(x) for x in input().split()]

# Отбираем двузначные и сортируем
dvuznachnie = [x for x in spisok if 10 <= x <= 99]
dvuznachnie.sort()

print(dvuznachnie)
