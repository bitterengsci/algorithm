#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (53.45%)
# Likes:    3097
# Dislikes: 97
# Total Accepted:    474.2K
# Total Submissions: 885.7K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
# 
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = list()
        candidates = sorted(list(set(candidates)))

        self.dfs(candidates, 0, target, [], results)

        return results
    
    def dfs(self, candidates, start_index, target, combination, results):

        # recursion's termination
        if target == 0:
            results.append(list(combination))   # deep copy
            # results.append(combination.copy())
        
        # recursion's breakdown
        for i in range(start_index, len(candidates)):
            if target < candidates[i]:
                break

            ### 解决duplicate的问题
                ## i != 0 是越界检测,
                ## 用 i != startIndex 不对
            # if i !=0 and candidates[i] == candidates[i-1]:
            #     continue

            combination.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], combination, results)
            combination.pop()  # backtracking  删去最后一个

        return 
        
# @lc code=end

