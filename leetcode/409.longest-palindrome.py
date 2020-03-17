#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (49.57%)
# Likes:    776
# Dislikes: 74
# Total Accepted:    126.6K
# Total Submissions: 255.4K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# palindrome: a word, phrase, or sequence that reads the same backwards as forwards
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = dict()
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1
        ANY_ODD = False
        longest_palindrome = 0
        for l in letters.keys():
            if letters[l] % 2 == 1:
                ANY_ODD = True
                longest_palindrome += letters[l] - 1
            else:
                longest_palindrome += letters[l]
        if ANY_ODD:
            return longest_palindrome + 1
        else:
            return longest_palindrome
# @lc code=end

s = Solution()
s.longestPalindrome("abccccdd")
print(s.longestPalindrome("bb"))

'''
>>> 17 // 3.0  # explicit floor division discards the fractional part
5.0
>>> 17 % 3  # the % operator returns the remainder of the division
2

dict.keys()

'''