#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (52.33%)
# Likes:    2367
# Dislikes: 62
# Total Accepted:    529.6K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its level order traversal as:
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        results = list()
        queue = [root]

        while queue:    # while len(queue) != 0:
            this_level = []
            next_level = []
            for node in queue:
                if node:
                    this_level.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            if len(this_level) > 0:
                results.append(this_level)
            queue = next_level

        return results
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        results = list()
        queue = [root]

        while queue:    # while len(queue) != 0:
            next_level = []
            results.append([node.val for node in queue if node])
            next_level += [node.left for node in queue if node]
            next_level += [node.right for node in queue if node]
            queue = next_level

        return results



# @lc code=end

