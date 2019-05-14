def pilesOfBoxes(boxesInPiles):
    # Write your code here
    pile = count_pile(boxesInPiles)
    key = list(pile.keys())
    key.sort()

    count = 0
    for i in range(1, len(key)):
        count += i * pile[key[i]]
    return count


def count_pile(boxesInPiles):
    dic = dict()
    for item in boxesInPiles:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    return dic


if __name__ == "__main__":
    pi = [777, 8]
    d = count_pile(pi)
    key = list(d.keys())
    key.sort()
    print(key)
    print(d)

    c = pilesOfBoxes(pi)
    print(c)
