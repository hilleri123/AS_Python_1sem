s = input()
result = ' '.join(word[0].upper() + word[1:-1] + word[-1].upper() for word in s.split())
print(result)
