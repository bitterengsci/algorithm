#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (44.96%)
# Likes:    3256
# Dislikes: 369
# Total Accepted:    537.2K
# Total Submissions: 1.2M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# Note:
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.

# @lc code=start
class Solution:

    # use backtracking, DFS
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = dict()
        letter_dict["2"] = ["a", "b", "c"]
        letter_dict["3"] = ["d", "e", "f"]
        letter_dict["4"] = ["g", "h", "i"]
        letter_dict["5"] = ["j", "k", "i"]
        letter_dict["6"] = ["m", "n", "o"]
        letter_dict["7"] = ["p", "q", "r", "s"]
        letter_dict["8"] = ["t", "u", "v"]
        letter_dict["9"] = ["w", "x", "y", "z"]

        output = [""]
        for i in range(len(digits)):
            output = zip(output, letter_dict[digits[i]])
            print(output)
        return output
        
# @lc code=end

