#-*-coding:utf-8-*-
'''
Given a binary tree, return the inorder traversal of its nodes' values.
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        result = []
        self.inorder(root, result)
        return result

    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)

    def inorderTraversal_NonRecursion(self, root):
        if root is None:
            return []

        # 创建一个 dummy node，右指针指向 root
        # 并放到 stack 里，此时 stack 的栈顶 dummy
        # 是 iterator 的当前位置
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        inorder = []
        # 每次将 iterator 挪到下一个点
        # 也就是调整 stack 使得栈顶到下一个点
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)

        return inorder


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)

s = Solution()
print(s.inorderTraversal(t))
print(s.inorderTraversal_NonRecursion(t))
