#-*-coding:utf-8-*-
'''
Description
    Given an array of integers that is already sorted in ascending order,
    find two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers
    such that they add up to the target, where index1 must be less than index2.
    Please note that your returned answers (both index1 and index2) are not zero-based.

    You may assume that each input would have exactly one solution.
'''

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):

        i, j = 0, len(nums) - 1
        while i != j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return i + 1, j + 1  # index 从1 开始的..
