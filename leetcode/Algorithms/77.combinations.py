#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (52.22%)
# Likes:    1193
# Dislikes: 60
# Total Accepted:    260.9K
# Total Submissions: 498.8K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = list(range(1, n+1))
        results = list()

        self.dfs(numbers, k, 0, [], results)

        return results
    
    def dfs(self, numbers, k, start_index, combination, results):
        if k == 0:
            results.append(list(combination))
        
        for i in range(start_index, len(numbers)):
            combination.append(numbers[i])
            self.dfs(numbers, k-1, i + 1, combination, results)
            combination.pop()
        
# @lc code=end


'''
self.dfs(numbers, k-1, i + 1, combination, results)
!!! 不是 self.dfs(numbers, k-1, start_index + 1, combination, results)
'''
