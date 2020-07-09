#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (28.46%)
# Likes:    6128
# Dislikes: 938
# Total Accepted:    610.1K
# Total Submissions: 2.1M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0
# 
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5

# @lc code=start
class Solution:

    # brute force
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 and nums2: 
            combined_list = nums1 + nums2
            combined_list.sort()
        elif nums1 and not nums2:
            combined_list = nums1
        elif not nums1 and nums2:
            combined_list = nums2
        else:
            return None
        if len(combined_list) % 2:
            return combined_list[len(combined_list)//2]
        else:
            return (combined_list[len(combined_list)//2] + combined_list[len(combined_list)//2 - 1]) / 2

    # binary search
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        pass
        
# @lc code=end

