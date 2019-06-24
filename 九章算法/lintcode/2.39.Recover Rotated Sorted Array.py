#-*-coding:utf-8-*-
'''
Description
    Given a rotated sorted array, recover it to sorted array in-place.

For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]

Example1:
    [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
Example2:
    [6,8,9,1,2] -> [1,2,6,8,9]

Challenge
    In-place, O(1) extra space and O(n) time.
'''
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        nums.sort()
