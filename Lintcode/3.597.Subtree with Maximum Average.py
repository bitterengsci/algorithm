#-*-coding:utf-8-*-
'''
Description
    Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

    LintCode will print the subtree which root is your return node.
    It's guaranteed that there is only one subtree with maximum average.

Note
    因为需要求平均数，所以要记录节点和以及接节点个数
    分治法计算每一颗子树的平均值，打擂台求出最大平均数的子树
'''
import sys
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    average, node = 0, None

    def findSubtree2(self, root):
        self.helper(root)
        return self.node

    def helper(self, root):
        if root is None:
            return 0, 0

        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)

        sum, size = left_sum + right_sum + root.val, left_size + right_size + 1

        if self.node is None or sum * 1.0 / size > self.average:
            self.node = root
            self.average = sum * 1.0 / size

        return sum, size


s = Solution()

root = TreeNode(1)
t1 = TreeNode(1)
t2 = TreeNode(2)
t_2 = TreeNode(-2)
t4 = TreeNode(4)
t_5 = TreeNode(-5)
t11 = TreeNode(11)

root.left = t_5
root.right = t11
t11.left = t4
t11.right = t_2
t_5.left = t1
t_5.right = t2

print(s.findSubtree2(root))
