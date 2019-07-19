#-*-coding:utf-8-*-
'''
Description
    Given a set of candidtate numbers candidates and a target number target.
    Find all unique combinations in candidates where the numbers sums to target.

    The same repeated number may be chosen from candidates unlimited number of times.

    * All numbers (including target) will be positive integers.
    * Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
    * Different combinations can be in any order.
    * The solution set must not contain duplicate combinations.
'''


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):

        result = []
        candidates = sorted(list(set(candidates)))

        # 初始调用
        # 把所有以 [] 开头的和为target的组合放入results
        self.dfs(candidates, 0, target, [], result)

        return result

    # 1.递归的定义
    # 找到所有以combination 开头的那些何为target的组合
    # 并放入results里, 其中剩余的需要加入combination里的数为remainTarget
    # 并且下一个可以加入combination中的数至少从candidates的startIndex开始
    def dfs(self, candidates, startIndex, remainTarget, combination, result):
        # if remainTarget < 0:
        #     return

        # 递归的出口
        if remainTarget == 0:
            result.append(list(combination))  # deep copy

        # 2.递归的拆解
                # subset问题 用 for i in range(startIndex+1, len(candidates))
        for i in range(startIndex, len(candidates)):
            if remainTarget < candidates[i]:
                break

            ### 解决duplicate的问题
                ## i != 0 是越界检测,
                ## 用 i != startIndex 不对
            # if i !=0 and candidates[i] == candidates[i-1]:
            #     continue

            combination.append(candidates[i])
            self.dfs(candidates, i, remainTarget - candidates[i], combination, result)
            combination.pop()  # backtracking  删去最后一个
