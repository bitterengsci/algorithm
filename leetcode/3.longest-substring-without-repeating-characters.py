#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.63%)
# Likes:    7999
# Dislikes: 488
# Total Accepted:    1.4M
# Total Submissions: 4.6M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 

# @lc code=start
class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        longest = 0

        for i in range(len(s)):
            unrepeated = 0
            letters = set()     # SC=O(min(n, 26)), charset has 26 in total
            j = i
            while j < len(s) and s[j] not in letters:
                letters.add(s[j])
                unrepeated += 1
                j += 1
            
            if unrepeated > longest:
                longest = unrepeated

        return longest
    
    def lengthOfLongestSubstring(self, s: str) -> int: 
        str_list = []
        max_length = 0
        
        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x)+1:]
                
            str_list.append(x)    
            max_length = max(max_length, len(str_list))
            
        return max_length
        
# @lc code=end

Solution().lengthOfLongestSubstring("pwwkew")

'''
* set.add(element)

Approach: Sliding Window

'''

