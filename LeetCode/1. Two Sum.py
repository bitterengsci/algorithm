#-*-coding:utf-8-*-
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution:
    # Brute Force    Time Complexity O(n2) Space Complexity O(1) (cuz O(0)=O(1))
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return i, j

    # Two-Pass Hash Table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            dic[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] in dic.keys():
                if i != dic[target - nums[i]]:
                    return i, dic[target - nums[i]]

    # One-Pass Hash Table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            if target - nums[i] in dic.keys():
                if i != dic[target - nums[i]]:
                    return dic[target - nums[i]], i
            else:
                dic[nums[i]] = i
