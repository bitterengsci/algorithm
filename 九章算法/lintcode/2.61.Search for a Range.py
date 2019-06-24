#-*-coding:utf-8-*-
'''
Description
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].
'''

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):     # not working yet
        # write your code here
        if len(A) == 0:
            return [-1, -1]
        start, end = 0, len(A) - 1

        while A[start] != A[end] and start + 1 < end:
            print(start, end, A[start], A[end])
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        print(start, end)

        if A[start] != target:
            start = end
        if A[end] != target:
            end = start

        if A[start] == target:
            return [start, end]
        else:
            return [-1, -1]

    def searchRange2(self, A, target):
        if len(A) == 0:
            return [-1, -1]

        # break it into 2 sub-problems

        # 1. find the first occurence of the target (lower_bound)
        # print('=== Part 1')
        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            # print(start, end, A[start], A[end])
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            lower_bound = start
        elif A[end] == target:
            lower_bound = end
        else:
            return [-1, -1]

        # 2. find the last occurence of the target (upper_bound)
        # print('=== Part 2')

        start, end = lower_bound, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            # print(start, end, A[start], A[end])
            if A[mid] > target:
                end = mid
            else:
                start = mid

        if A[end] == target:     # 注意这个地方的if elif 和 part 1的是反的！！！
            upper_bound = end
        elif A[start] == target:
            upper_bound = start
        else:
            return [-1, -1]

        return [lower_bound, upper_bound]


s = Solution()
print(s.searchRange2([-1,0,1,2,2,2,3,3,3,4,4,4,5,5,6,90,92,93,101], 2))
