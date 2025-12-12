#если матрицы записаны так:
#1 2 3
#4 5 6

#7 8 9
#1 2 3


def read_matrices(filename):
    matrices = []
    with open(filename, "r", encoding="utf-8") as f:
        matrix = []
        for line in f:
            line = line.strip()
            if line:
                matrix.append(list(map(int, line.split())))
            else:
                if matrix:
                    matrices.append(matrix)
                    matrix = []
        if matrix:
            matrices.append(matrix)
    return matrices


def write_matrices(filename, matrices):
    with open(filename, "w", encoding="utf-8") as f:
        for m in matrices:
            for row in m:
                f.write(" ".join(map(str, row)) + "\n")
            f.write("\n")   # разделитель матриц


# ---- Основная программа ----

threshold = int(input("Введите пороговое число: "))

mat1 = read_matrices("file1.txt")   # k матриц m×n
mat2 = read_matrices("file2.txt")   # l матриц m×n

# переносим матрицы из file1 → file2
remaining = []
for m in mat1:
    if sum(m[0]) > threshold:
        mat2.append(m)
    else:
        remaining.append(m)

mat1 = remaining  # обновляем первый файл

# записываем результат обратно
write_matrices("file1.txt", mat1)
write_matrices("file2.txt", mat2)

# выводим содержимое файлов
print("Содержимое file1.txt:")
for m in mat1:
    print(m)

print("\nСодержимое file2.txt:")
for m in mat2:
    print(m)
