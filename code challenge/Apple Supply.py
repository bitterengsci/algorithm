M = 5
X = 500

apples = [150, 80, 80, 120, 200]
apples = [[x, y] for x, y in sorted(enumerate(apples), key = lambda x: -x[1])]

apple_to_supply = X
apples_adjusted = []

for i in apples:
    apple_num_class = i[0]
    apple_in_class = i[1]
    if apple_to_supply >= apple_in_class:
        apples_adjusted.append([apple_num_class, apple_in_class])
        apple_to_supply -= apple_in_class
    else:
        apples_adjusted.append([apple_num_class, min(apple_to_supply, apple_in_class)])
        apple_to_supply -= min(apple_to_supply, apple_in_class)

apples = [y for x, y in sorted(apples, key = lambda x: x[0])]
apples_adjusted = [y for x, y in sorted(apples_adjusted, key = lambda x: x[0])]

for i in range(M):
    print(apples[i], apples_adjusted[i], apples[i] - apples_adjusted[i])