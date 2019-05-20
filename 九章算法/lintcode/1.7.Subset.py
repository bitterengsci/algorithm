'''
17. Subsets 全子集问题 
Given a set of distinct integers, return all possible subsets.
- Elements in a subset must be in non-descending order.
- The solution set must not contain duplicate subsets.

Example
Example 1:
Input: [0]
Output:
[
  [],
  [0]
]

Example 2:
Input: [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Challenge: Can you do it in both recursively and iteratively?
算法: DFS (深度优先搜索)

recursion = 递归 (两种理解: 算法-- DFS; 程序的实现方式--函数自己调用了自己)
backtracking = 回溯法
'''

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        