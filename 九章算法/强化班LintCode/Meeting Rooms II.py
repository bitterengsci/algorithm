"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    # Approach 1: using heap (heapq)
    def minMeetingRooms(self, intervals):
        # points = []
        # for interval in intervals:
        #     points.append([interval.start, interval.end])
        
        points = intervals
        # sort
        points.sort(key=lambda x: (x[0], x[1]))

        endtime = []
        for start, end in points:
            if not endtime: # no room assigned, endtime empty (edge case)
                heapq.heappush(endtime, end)
            else:
                heapq.heapify(endtime)
                # earliest = heapq.nsmallest(1, endtime)
                earliest = heapq.heappop(endtime)
                if start < earliest:
                    heapq.heappush(endtime, earliest)
                    heapq.heappush(endtime, end)
                else:
                    heapq.heappush(endtime, end)

        return len(endtime)
        

    # Approach 2: using list
    def minMeetingRooms(self, intervals):
        points = []
        for interval in intervals:
            points.append([interval.start, interval.end])
    
        # sort
        points.sort(key=lambda x: (x[0], x[1]))

        endtime = []
        for start, end in points:
            if not endtime: # no room assigned, endtime empty
                endtime.append(end)
            else:
                endtime.sort()
                if start < endtime[0]:
                    endtime.append(end)
                else:
                    endtime[0] = end

        return len(endtime)

Solution().minMeetingRooms([(0,30),(5,10),(15,20)])