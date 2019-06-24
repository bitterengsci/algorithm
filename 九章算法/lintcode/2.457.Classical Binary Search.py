'''
Description

Find any position of a target number in a sorted array. Return -1 if target does not exist.

'''

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        if nums == []:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2    # equivalent to (start + end) / 2
                                                # but can avoid overflow when s and e are both large
            nums_mid = nums[mid]      # save time: to avoid indexing the list nums twice
            if nums_mid > target:
                end = mid
            elif nums_mid == target:
                return mid
            else:
                start = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1
