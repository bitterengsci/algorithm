#-*-coding:utf-8-*-
'''
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

Note:
    考虑mid在递增区间还是递减区间 (画图~)

    1 2 3 4 5 4 3 2 1
    o o o o x x x x x
    找ooxx的条件, first of x 或者 last of o (推荐first of x, 因为last of o 题型容易出现死循环)

'''

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid == 0:
                pre, next = nums[mid], nums[mid + 1]
            elif mid == len(nums):
                pre, next = nums[mid - 1], nums[mid]
            else:
                pre, next = nums[mid - 1], nums[mid + 1]

            if pre < nums[mid] < next:
                start = mid
            elif pre > nums[mid] > next:
                end = mid
            else:
                return nums[mid]

        return max(nums[start], nums[end])
