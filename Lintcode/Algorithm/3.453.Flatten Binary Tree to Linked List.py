#-*-coding:utf-8-*-
'''
Description
    Flatten a binary tree to a fake "linked list" in pre-order traversal.
    Here we use the right pointer in TreeNode as the next pointer in ListNode.

    Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

Challenge
    Do it in-place without any extra memory.
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution_my_soln:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):

        result = self.preorder(root)
        if not result:
            return root

        for i in range(len(result) - 1):
            result[i].left = None
            result[i].right = result[i + 1]

        result[-1].left = None


    def preorder(self, root):
        if not root:
            return []

        left = self.preorder(root.left)
        right = self.preorder(root.right)

        return [root] + left + right


# 九章算法答案
class Solution:
    last_node = None

    def flatten(self, root):
        if root is None:
            return

        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root

        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)


    # 使用 Divide & Conquer
    # 分治函数 return 这个 tree 的最后一个点
    def flatten2(self, root):
        self.helper(root)

    # restructure and return last node in preorder
    def helper(self, root):
        if root is None:
            return

        left_last = self.helper(root.left)
        right_last = self.helper(root.right)

        # connect
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        if right_last is not None:
            return right_last

        if left_last is not None:
            return left_last

        return root
