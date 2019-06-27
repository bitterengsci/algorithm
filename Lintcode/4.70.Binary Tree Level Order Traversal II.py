#-*-coding:utf-8-*-
'''
Description
    Given a binary tree, return the bottom-up level order traversal of its nodes' values.
    (ie, from left to right, level by level from leaf to root).
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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    # inspired by Question 69
    def levelOrderBottom(self, root):
        if root is None:
            return []

        result = []
        queue = [root]
        while len(queue) != 0:
            level = [node.val for node in queue]
            next_level = []
            for _ in range(len(level)):
                node = queue.pop(0)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.insert(0, level)
            queue = next_level
        return result

    #
    def levelOrderBottom2(self, root):
        result = []
        if not root:
            return result

        queue = [root]
        while queue:
            next_level = []
            result.append([n.val for n in queue])
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
        return list(reversed(result))
