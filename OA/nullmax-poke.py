# while 1:
#     def shuffle(n):
#         new_list = list()
#         card = list(range(1, n + 1))
#
#         while len(card) > 0:
#             new_list.append(card.pop(0))
#             if len(card) > 0:
#                 card.append(card.pop(0))
#         for i in new_list:
#             print(i)
#
#     cardList = list()
#     s = input()
#
#     if s != "":
#         for i in s.split("\n"):
#             cardList.append(i)
#     else:
#         break
#     numList = int(cardList.pop(0))
#
#     for i in cardList:
#         print(shuffle(int(i)))

def shuffle(n):
    new_str = str()
    card = list(range(1, n + 1))

    while len(card) > 0:
        new_str += str(card.pop(0)) + " "
        # new_list.append(card.pop(0))
        if len(card) > 0:
            card.append(card.pop(0))
    new_str = new_str[: -1]
    print(new_str)

if __name__ == "__main__":
    shuffle(7)
