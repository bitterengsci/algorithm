#-*-coding:utf-8-*-
'''
Description
    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as a binary tree
    in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        if root is None:
            return True
        if abs(self.calculate_height(root.left) - self.calculate_height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

    def calculate_height(self, root):
        if root is None:
            return 0
        left_height = self.calculate_height(root.left)
        right_height = self.calculate_height(root.right)

        return max(left_height, right_height) + 1

    # 九章算法答案
    def isBalanced2(self, root):
        balanced, _ = self.validate(root)
        return balanced

    def validate(self, root):
        if root is None:
            return True, 0

        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0

        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1


t = TreeNode(2)
t.left = TreeNode(3)
t_root = TreeNode(1)
t_root.right = t

s = Solution()
print(s.isBalanced(t_root))

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)
t10 = TreeNode(10)
t11 = TreeNode(11)
t12 = TreeNode(12)

t7.left = t11
t7.right = t12
t5.left = t7
t5.right = t8
t6.left = t9
t6.right = t10
t3.left = t5
t3.right = t6
t1.left = t2
t1.right = t3

t2.left = t4

print(s.isBalanced(t1))
