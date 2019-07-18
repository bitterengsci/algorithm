#-*-coding:utf-8-*-
'''
Description
    Given a binary search tree and a new tree node, insert the node into the tree.
    You should keep the tree still be a valid binary search tree.  (注意: BST不需要balanced!!!)

    You can assume there is no duplicate values in this tree + node.

Challenge
    Can you do it without recursion?


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
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if not root:
            return node

        if root.val > node.val:
            if not root.left:
                root.left = node
            else:
                self.insertNode(root.left, node)

        else:
            if not root.right:
                root.right = node
            else:
                self.insertNode(root.right, node)

        return root


    # No Recursion (TODO)

