'''
Description

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.

Note:
First position <= Last Number
(WRONG: First position <= or < First Number)
'''
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] > nums[start] and nums[mid] > nums[end]:
                start = mid
            # if nums[mid] < nums[start] and nums[mid] < nums[end]:
            #     end = mid
            # if nums[mid] > nums[start] and nums[mid] < nums[end]:
            #     end = mid
            else:
                end = mid

        minimum = min(nums[start], nums[end])

        return minimum
