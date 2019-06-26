#-*-coding:utf-8-*-
'''
Given a binary tree, return the preorder traversal of its nodes' values.
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        result = []
        self.preorder(root, result)
        return result

    def preorder(self, root, result):
        if root:
            result.append(root.val)
            self.preorder(root.left, result)
            self.preorder(root.right, result)

    def preorderTraversal_NonRecursion(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)

s = Solution()
print(s.preorderTraversal(t))
print(s.preorderTraversal_NonRecursion(t))
