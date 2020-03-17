#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.63%)
# Likes:    2952
# Dislikes: 4658
# Total Accepted:    982.6K
# Total Submissions: 3.8M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# Input: 123
# Output: 321
# 
# 
# Example 2:
# Input: -123
# Output: -321
# 
# 
# Example 3:
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 

# @lc code=start
class Solution:

    # Pop and Push Digits 
    # TC=O(log(x)), roughly log10(x) digits in x
    # SC can be optimized to O(1)
    def reverse1(self, x: int) -> int:
        if x >= 2 ** 31 - 1 or x <= -2 ** 31: 
            return 0

        sign = abs(x) == x  # False is negative
        x = abs(x)
        digits = list()
        while x > 10:
            digits.append(x % 10)
            x = x // 10
        
        i = 1
        while digits:
            x += 10 ** i * digits.pop(-1)
            i += 1

        x = x if sign else -x

        if x >= 2 ** 31 - 1 or x <= -2 ** 31: 
            return 0
        else:
            return x
    # convert to string first, then str[:, -1]
    def reverse(self, x: int) -> int:
        if x > 0:  # positive numbers  
            a =  int(str(x)[::-1])  
        if x <= 0:  # negative numbers  
            a = - int(str(abs(x))[::-1])  
        
        # 32 bit overflow   
        return a if a in range(-2**31, 2**31 - 1) else 0

        # @lc code=end

Solution().reverse(123)

'''
How to deal with overflow?

'''