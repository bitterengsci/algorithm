#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (50.59%)
# Likes:    479
# Dislikes: 42
# Total Accepted:    106K
# Total Submissions: 209.5K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given a sorted (in ascending order) integer array nums of n elements and a
# target value, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# 
# Note:
# 
# 
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
        
# @lc code=end
print(Solution().search([5], -5))

'''
>>> 1 < 1 
False
'''
