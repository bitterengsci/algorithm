
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer

for case in range(1, t + 1):
    N = int(input()) # number of activities

    schedule = ""

    # avaliability
    Cameron, Jamie = 0, 0

    pairs = []

    for i in range(N):
        # start, end = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        pairs.append([int(s) for s in input().split(" ")])
    
    # enumerate(pairs) gives you a list containing tuples of (index, value)
    # pairs = sorted( (e, i) for i, e in enumerate(pairs))
    indices = sorted(range(len(pairs)), key=lambda k: pairs[k])
    
    for i in indices:
        start, end  = pairs[i]
        if start >= Cameron:
            schedule += "C"
            Cameron = end
        elif start >= Jamie:
            schedule += "J"
            Jamie = end
        else:
            schedule = "IMPOSSIBLE"
            continue
    
    schedule = [schedule[i] for i in indices]
    schedule = schedule.join()
    print(schedule)
    ### output
    print("Case #{}: {}".format(case, schedule))
    # check out .format's specification for more formatting options

# 4
# 3
# 360 480
# 420 540
# 600 660
# 3
# 0 1440
# 1 3
# 2 4
# 5
# 99 150
# 1 100
# 100 301
# 2 5
# 150 250
# 2
# 0 720
# 720 1440