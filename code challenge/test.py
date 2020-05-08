

pairs = [[2, 22], [0, 33], [1, 44]]

indices = sorted(range(len(pairs)), key=lambda k: pairs[k])
print(indices)
print(pairs)

for i in indices:
    print(pairs[i])