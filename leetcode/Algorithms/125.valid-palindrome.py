#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (34.23%)
# Likes:    928
# Dislikes: 2535
# Total Accepted:    497.6K
# Total Submissions: 1.5M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# Example 2:
# 
# Input: "race a car"
# Output: false
# 
#

# @lc code=start
class Solution:
    def isPalindrome_1(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while j - i > 0:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.findall(r'\w+', s)
        s = ''.join(s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right-1
        return True
# @lc code=end

'''
* two pointer, i starts from 0, j starts from len-1
* two pointers: consider the length of string even or odd !!!
* for two pointers problem, take care of index out of range error!

* string.isalnum() returns True if the string contains only alphanumeric characters
* re.findall(r'REGEX',s)
    - Regular Expression: Python re module (import re)
        Reference: https://www.w3schools.com/python/python_regex.asp

'''
s = Solution()
print(s.isPalindrome("race a car"))
print(s.isPalindrome("A man, a plan, a canal: Panama"))