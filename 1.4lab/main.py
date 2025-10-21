# Вводим список
spisok = [5, 2, 8, 1, 9, 3]

# Первый элемент считаем самым маленьким и самым большим
min_element = spisok[0]
max_element = spisok[0]

# Проверяем каждый элемент
for i in range(len(spisok)):
    # Если нашли элемент меньше минимального
    if spisok[i] < min_element:
        min_element = spisok[i]
    
    # Если нашли элемент больше максимального
    if spisok[i] > max_element:
        max_element = spisok[i]

# Выводим ответ
print("Самый маленький:", min_element)
print("Самый большой:", max_element)
