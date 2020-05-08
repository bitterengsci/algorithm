# def removeCoveredIntervals(intervals):
#     # Sort by start point.
#     # If two intervals share the same start point
#     # put the shorter one to be the first.
#     intervals.sort(key = lambda x: (x[0], x[1]))
#     # intervals.sort(key = lambda x: (x[0], x[1]))  # put the longer one to be the first.
#     count = 0
    
#     prev_end = 0
#     for _, end in intervals:
#         # if current interval is not covered by the previous one
#         if end > prev_end:
#             count += 1    
#             prev_end = end
#     return count

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer

for case in range(1, t + 1):
    N = int(input()) # number of activities

    # avaliability
    Cameron, Jamie = 0, 0

    pairs = []

    for i in range(N):
        # start, end = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        pairs.append([int(s) for s in input().split(" ")])
    
    # enumerate(pairs) gives you a list containing tuples of (index, value)
    # pairs = sorted( (e, i) for i, e in enumerate(pairs))
    indices = sorted(range(len(pairs)), key=lambda k: pairs[k])
    
    schedule_list = []
    for i in indices:
        start, end  = pairs[i]
        if start >= Cameron:
            schedule_list.append("C")
            Cameron = end
        elif start >= Jamie:
            schedule_list.append("J")
            Jamie = end
        else:
            schedule = "IMPOSSIBLE"
            continue
    
    if len(schedule_list) == N:
        schedule = ""
        schedule_list = [schedule_list[i] for i in indices]
        schedule = schedule.join(schedule_list)

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