#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.78%)
# Likes:    5642
# Dislikes: 474
# Total Accepted:    816K
# Total Submissions: 2.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# Example 2:
# 
# Input: "cbbd"
# Output: "bb"
#

# @lc code=start
import re
class Solution:
    def longestPalindrome(self, s: str) -> str:  # N^3 answer --> Time Limit Exceeded
        longestPalindrome = "" # output if no answer? none, "" or False
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                if self.validPalindrome(s[i:j]) and j-i > len(longestPalindrome):
                    longestPalindrome = s[i:j]
        return longestPalindrome

    def validPalindrome(self, sub: str) -> bool:
        sub = sub.lower()
        sub = re.findall(r'\w+', sub)
        sub = ''.join(sub)
        left, right = 0, len(sub)-1
        while left < right:
            if sub[left] != sub[right]:
                return False
            left, right = left+1, right-1
        return True
# @lc code=end
s = Solution()
print(s.longestPalindrome("a"))

'''
Approach 1: Brute Force, T=O(N3), S=O(1)
* slicing [i: j], from index i to index j-1
* Time Limit Exceeded

Approach 2: Expand Around Center

'''
