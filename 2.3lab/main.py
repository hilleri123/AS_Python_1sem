def Bell(L):
    L = sorted(L)
    res = []
    left, right = 0, len(L) - 1

    while left <= right:
        res.append(L[left])      # минимальный — в начало
        left += 1
        if left <= right:
            res.append(L[right]) # следующий минимальный — в конец
            right -= 1

    return res
#пример
print(Bell([5, 1, 4, 2, 3]))
