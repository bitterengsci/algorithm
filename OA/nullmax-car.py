# def carlist():
#     numCar = int(input("Enter your number of Car: "))
#     carList = list()
#     for i in range(numCar):
#         name_car = input("Name your " + str(i+1) + "th Car: ")
#         carList.append(name_car)
#     carList.sort()
#
#     for i in carList:
#         print(i)
#
# if __name__ == "__main__":
#     carlist()

while 1:
    carList = list()
    s = input()

    if s != "":
        for i in s.split("\n"):
            carList.append(i)
    else:
        break
    numCar = int(carList.pop(0))

    carList.sort()
    for i in carList:
        print(i)
