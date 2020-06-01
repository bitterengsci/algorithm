'''
Given a target number and an integer array A sorted in ascending order, 
find the index i in A such that A[i] is closest to the given target.

Return -1 if there is no element in the array.
'''
class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        if not A: return -1

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > target: # find the one closest to and smaller than target first
                end = mid
            else:
                start = mid

        if A[end] - target > target - A[start]:
            return start
        else:
            return end