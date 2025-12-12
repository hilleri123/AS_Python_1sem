def merge_lists_with(list1, list2, merge_function=None):
    if merge_function:
        return [merge_function(x, y) for x, y in zip(list1, list2)]
    return list1 + list2
#примеры
def merge_lists_with(list1, list2, merge_function=None):
    if merge_function:
        return [merge_function(x, y) for x, y in zip(list1, list2)]
    return list1 + list2
#б
def extract_digits(strings, digits_only=False):
    if not digits_only:
        return strings
    return [''.join(ch for ch in s if ch.isdigit()) for s in strings]
#примеры
print(extract_digits(['a1b2', 'c3d4']))               # ['a1b2', 'c3d4']
print(extract_digits(['a1b2', 'c3d4'], True))         # ['12', '34']
#в
def filter_even_numbers(*nums):
    return [n for n in nums if n % 2 == 0]
#примеры
print(filter_even_numbers(1, 2, 3, 4, 5, 6))   # [2, 4, 6]
print(filter_even_numbers(7, 9, 11))           # []
#г
def sorted_positive_numbers(*nums):
    return sorted([n for n in nums if n > 0], reverse=True)
#примеры
print(sorted_positive_numbers(-1, 3, -5, 7, 0))   # [7, 3]
print(sorted_positive_numbers(-10, -20))          # []
