#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (45.12%)
# Likes:    13904
# Dislikes: 509
# Total Accepted:    2.7M
# Total Submissions: 5.9M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# @lc code=start
class Solution:
    # Brute Force    Time Complexity O(n2) Space Complexity O(1) (cuz O(0)=O(1))
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return i, j

    # Two-Pass Hash Table
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
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
        
# @lc code=end