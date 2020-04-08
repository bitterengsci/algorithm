# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer, number of input tests

for case in range(1, t + 1):
    N = int(input())
    trace, repeated_rows, repeated_cols = 0, 0, 0
    columns = [set([]) for _ in range(N)]

    for i in range(N):
        entries = [int(s) for s in input().split(" ")]  # read a list of integers
        trace += entries[i]
        if len(entries) != len(set(entries)):
            repeated_rows += 1
        for c in range(N):
            columns[c].add(entries[c])
        repeated_cols = sum([True if len(columns[cc]) != N else False for cc in range(N)])

    ### output
    print("Case #{}: {} {} {}".format(case, trace, repeated_rows, repeated_cols))