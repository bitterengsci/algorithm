"""
Give two users' ordered online time series, 
and each section records the user's login time point x and offline time point y. 
Find out the time periods when both users are online at the same time, 
and output in ascending order. you need return a list of intervals.
"""

# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """

    def timeIntersection_jiuzhang(self, seqA, seqB):
        points = []
        for interval in seqA + seqB:
            points.append((interval.start, 1))
            points.append((interval.end, -1))
            
        online = 0
        intervals = []
        last_timestamp = None
        for timestamp, delta in sorted(points):
            if online == 2:
                self.merge_to(intervals, last_timestamp, timestamp)
            online += delta
            last_timestamp = timestamp
                
        return intervals
        
    def merge_to(self, intervals, start, end):
        if start is None or start == end:
            return
        
        if intervals and intervals[-1].end == start:
            intervals[-1].end = end
            return
        
        intervals.append(Interval(start, end))

    # Approach: Sweep Line
    # 遇到start，count++，遇到end，count--
    # intersection就是找出所有时刻(x, x+1)，其中x时刻count=2，x+1时刻的count=1或0
    def timeIntersection_my(self, seqA, seqB):
        # seqA.sort()
        # seqB.sort()
        # timeA, timeB = [], []
        # for a in seqA:
        #     timeA.append([a[0], 1])
        #     timeA.append([a[1], -1])
        # for b in seqB:
        #     timeB.append([b[0], 1])
        #     timeB.append([b[1], -1])

        points = []
        for a in seqA:
            points.append((a.start, 1))
            points.append((a.end, -1))
        for b in seqB:
            points.append((b.start, 1))
            points.append((b.end, -1))
        
        result = []
        start, end = 0, 0
        count = 0
        for time, delta_count in sorted(points):
            count += delta_count
            if count == 2:
                start = time
            if count == 1 and delta_count == -1:
                end = time
                result.append(Interval(start, end))
                # start = 0
                # end = 0
        return result


    # Approach: two pointer
    def timeIntersection(self, A, B):
        output = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            a, b = A[i], B[j]
            if min(a.end, b.end) >= max(a.start, b.start):
                output.append(Interval(max(a.start, b.start), min(a.end, b.end)))
            
            if a.end <= b.end: 
                 i += 1
            if a.end >= b.end:
                j += 1
        
        return output


seqA = [Interval(1, 3), Interval(5, 7)]
seqB = [Interval(2, 2.5), Interval(4, 5.5)]

result = Solution().timeIntersection_my(seqA, seqB)

for i in result:
    print(i.start, i.end)