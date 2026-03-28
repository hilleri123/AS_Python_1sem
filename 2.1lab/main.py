#a
d = {'b': 1, 'a': 2, 'c': 3}
d = dict(sorted(d.items()))
print(d)
#б
d = {'a': 1, 'b': 2, 'c': 3}

for k, v in d.items():
    print(f"key: {k}, value: {v}, item: ({k}, {v})")
#в
d = {'a': '1', 'b': '2', 'c': '3.0'}

for k, v in d.items():
    d[k] = int(v) if v.isdigit() else float(v)

print(d)
