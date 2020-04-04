#-*-coding:utf-8-*-
'''
Description
    Given an array num and a number target.
    Find all unique combinations in num where the numbers sum to target.

    * Each number in num can only be used once in one combination.
    * All numbers (including target) will be positive integers.
    * Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
    * Different combinations can be in any order.
    * The solution set must not contain duplicate combinations.
'''
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        result = []
        num.sort()

        self.dfs(num, 0, target, [], result)

        return result


    def dfs(self, candidates, startIndex, remainTarget, combination, result):
        if remainTarget == 0:
            result.append(list(combination))

        for i in range(startIndex, len(candidates)):

            # 去重复  [1, 1, 1, 2] target 4 仅选择 [1a, 1b, 2]
            # 滤去 [1a, 1c, 2] 和 [1b, 1c, 2]
            if i != startIndex and candidates[i] == candidates[i - 1]:
                continue

            if remainTarget < candidates[i]:
                break

            combination.append(candidates[i])
            self.dfs(candidates, i + 1, remainTarget - candidates[i], combination, result)
            combination.pop()
