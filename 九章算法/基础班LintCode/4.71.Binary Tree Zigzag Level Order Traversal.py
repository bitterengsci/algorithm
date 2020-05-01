#-*-coding:utf-8-*-
'''
Description
    Given a binary tree, return the zigzag level order traversal of its nodes' values.
    (ie, from left to right, then right to left for the next level and alternate between).
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):

        result = []
        if root is None:
            return result

        queue = [root]
        isReverse = 1

        while queue:
            if isReverse == -1:
                result.append(list(reversed([node.val for node in queue])))
            else:
                result.append([node.val for node in queue])

            isReverse *= -1

            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level

        return result

    # 九章算法
    def preorder(self, root, level, res):
        if root:
            if len(res) < level + 1:res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)

    def zigzagLevelOrder2(self, root):
        results = []
        self.preorder(root, 0, results)
        return results
