# читаем исходные числа
with open("f.txt", "r") as f:
    nums = [int(x) for x in f.read().split()]

positives = [x for x in nums if x > 0]
negatives = [x for x in nums if x < 0]

# чередуем числа
result = []
while positives and negatives:
    result.append(positives.pop())
    result.append(negatives.pop())

# записываем в файл g
with open("g.txt", "w") as g:
    g.write(" ".join(map(str, result)))
