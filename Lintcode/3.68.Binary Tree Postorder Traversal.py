#-*-coding:utf-8-*-
'''
Given a binary tree, return the postorder traversal of its nodes' values.
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        result = []
        self.postorder(root, result)
        return result

    def postorder(self, root, result):
        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result.append(root.val)


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)

s = Solution()
print(s.postorderTraversal(t))
