#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (34.85%)
# Likes:    1440
# Dislikes: 4158
# Total Accepted:    418.2K
# Total Submissions: 1.2M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# @lc code=start
import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        block_size = numRows + numRows - 2  # 3 -> 4, 4 -> 6
        num_block = math.ceil(len(s) / block_size)
            
        for i in range(block_size//2): 
            for j in range(num_block):
                print(i, j)
                if j * block_size + i < len(s):
                    result += s[j * block_size + i]
                    print(j * block_size + i)
                if (j + 1) * block_size - i < len(s):
                    result += s[(j + 1) * block_size - i - 1]
                    print((j + 1) * block_size - i - 1)
                # print(result)

        for j in range(num_block):
            if j + block_size/2 < len(s):
                result += s[j + block_size//2]
            print(result)

        return result
# @lc code=end

Solution().convert("PAYPALISHIRING", 3)
# 0 4 8 12 1 3 5 7 9 11 13 2 6 10
# "PAHNAPLSIIGYIR"