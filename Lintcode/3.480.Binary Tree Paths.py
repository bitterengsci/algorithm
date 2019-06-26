#-*-coding:utf-8-*-
'''
Given a binary tree, return all root-to-leaf paths.

Note
    递归三要素: 递归的定义 拆解 出口
    DFS → return 所有路径 → D &C / Traverse
    二叉树 → 拆成左右子树 divide, 然后conquer (merge)
    出口通常只用处理 root==null
    所有二叉树一定要验证, 当root只有一个点时, 答案是否正确
    叶子节点, 单独处理 root.left==null && root.right==null
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    # Traversal 版本的 DFS
    def binaryTreePaths(self, root):
        if root is None:
            return []
        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if node.left is None and node.right is None:
            result.append('->'.join(path))

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()

        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()

    # Divider Conquer 版本的 DFS
    def binaryTreePaths2(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        paths = []
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + '->' + path)

        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + '->' + path)

        return paths


t1 = TreeNode(2)
t1.right = TreeNode(5)
t = TreeNode(1)
t.right = TreeNode(3)
t.left = t1

s = Solution()
print(s.binaryTreePaths(t))
print(s.binaryTreePaths2(t))
