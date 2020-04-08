# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer, number of input tests

for case in range(1, t + 1):
    s = str(input())

    nested_s = ""
    s = "0" + s + "0"

    for i in range(1, len(s)-1):
        nested_s += "(" * (int(s[i]) - int(s[i-1]) if int(s[i]) > int(s[i-1]) else 0) + s[i] \
                    + ")" * (int(s[i]) - int(s[i+1]) if int(s[i]) > int(s[i+1]) else 0)

    ### output
    print("Case #{}: {}".format(case, nested_s))