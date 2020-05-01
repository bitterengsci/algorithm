#-*-coding:utf-8-*-
'''
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Note
    方法一 Traverse + Divide Conquer  (遍历需要全局变量)   DS和T并不互补, 可以结合使用
	    计算sum of subtree (左右子树之和+root), 可以把每个点扫一遍加起来
    方法二 只用Divide Conquer 来实现
'''
import sys

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    # Divide Conquer + Traverse 的方法
    # Traversal遍历需要全局变量
    def findSubtree(self, root):
        # write your code here
        self.minimum_weight, self.subtree_root = sys.maxsize, None

        self.findsub(root)

        return self.subtree_root

    def findsub(self, root):
        if root is None:
            return 0

        left_weight = self.findsub(root.left)
        right_weight = self.findsub(root.right)
        root_weight = left_weight + right_weight + root.val

        if root_weight < self.minimum_weight:
            self.minimum_weight, self.subtree_root = root_weight, root

        return root_weight

    # Divide Conquer
    def findSubtree2(self, root):
        minimum, subtree, sum = self.helper(root)
        return subtree

    def helper(self, root):
        if root is None:
            return sys.maxsize, None, 0

        left_minimum, left_subtree, left_sum = self.helper(root.left)
        right_minimum, right_subtree, right_sum = self.helper(root.right)

        sum = left_sum + right_sum + root.val
        if left_minimum == min(left_minimum, right_minimum, sum):
            return left_minimum, left_subtree, sum
        if right_minimum == min(left_minimum, right_minimum, sum):
            return right_minimum, right_subtree, sum

        return sum, root, sum
