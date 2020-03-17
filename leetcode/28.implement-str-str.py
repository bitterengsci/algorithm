#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.80%)
# Likes:    1303
# Dislikes: 1704
# Total Accepted:    585.3K
# Total Submissions: 1.7M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#

# @lc code=start
class Solution:
    def strStr_1(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                d_i = 0
                while d_i + i < len(haystack) and d_i < len(needle):
                    if haystack[i + d_i] == needle[d_i]:
                        d_i += 1
                    else:
                        break
                if d_i == len(needle):
                    return i
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1
# @lc code=end


'''
Problem of sliding window, two pointers

* string slicing
* edge case: empty string (one empty string, both empty strings..)
* When dealing with two strings, take care of both index outofbound
* Time Limit Exceeded:

TODO: Rabin Karp: Constant Time Slice
'''