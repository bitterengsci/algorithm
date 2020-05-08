import sys

name = "A-small"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = input().split()
    cmd = line[0]
    n = int(line[1])
    a = [float(x) for x in line[2:]]

    if cmd == "median":
        a.sort()
        res = a[n // 2]
    elif cmd == "mean":
        res = sum(a) / float(len(a))

    print("Case #" + str(testCase) + ": " + ("%.10f" % res))