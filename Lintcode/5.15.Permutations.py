#-*-coding:utf-8-*-
'''
Description
    Given a list of numbers, return all possible permutations.

    * You can assume that there is no duplicate numbers in the list.
'''


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        results = []
        self.dfs(nums, [], [], results)
        return results

    # 递归的定义
    # 找到以所有permutation开头的排列
    def dfs(self, nums, permutation, used, results):

        # 用used 记录permutation已经使用过哪些数
        # 或者用一个新的数组, 记录使用过数字的下标

        # 3.递归的出口
        # 找够了所有的数
        if len(nums) == len(used):
            results.append(list(permutation))      # dfs 一定要使用deepcopy

        # 2.递归的拆解
        for i in nums:
            if i not in used:
                permutation.append(i)
                used.append(i)
                self.dfs(nums, permutation, used, results)
                permutation.remove(i)
                used.remove(i)
