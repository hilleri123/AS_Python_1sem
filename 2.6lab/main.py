# matrix_utils.py

def min_element(matrix):
    return min(min(row) for row in matrix)

def max_element(matrix):
    return max(max(row) for row in matrix)

def sum_matrix(matrix):
    return sum(sum(row) for row in matrix)

def sum_row(matrix, row_index):
    return sum(matrix[row_index])
#пример
import matrix_utils as mu

m = [
    [1, 5, 3],
    [7, 2, 9],
    [4, 6, 8]
]

print(mu.min_element(m))   # 1
print(mu.max_element(m))   # 9
print(mu.sum_matrix(m))    # 45
print(mu.sum_row(m, 1))    # 18
