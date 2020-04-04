#-*-coding:utf-8-*-
'''
Description
    Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
    The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

    Assume two nodes are exist in tree.

Note
    考点：
        搜索
        lca
        题解：递归查找A和B， 找到A和B第一次在同一棵子树中的子树根节点即是LCA。
'''
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        if root is None:
            return None

        if A.val in self.descendants(root.left) and B.val in self.descendants(root.left):
            return self.lowestCommonAncestor(root.left, A, B)
        elif A.val in self.descendants(root.right) and B.val in self.descendants(root.right):
            return self.lowestCommonAncestor(root.right, A, B)
        else:
            return root

    def descendants(self, root):
        if root is None:
            return []

        left_descendants = self.descendants(root.left)
        right_descendants = self.descendants(root.right)

        return [root.val] + left_descendants + right_descendants

    # 九章算法答案
    def lowestCommonAncestor2(self, root, A, B):
        # A & 下面有B => A
        # B & 下面有A => B
        # A & 下面啥都没有 => A
        # B & 下面啥都有 => B
        if root is None:
            return None

        if root == A or root == B:
            return root

        left_result = self.lowestCommonAncestor(root.left, A, B)
        right_result = self.lowestCommonAncestor(root.right, A, B)

        # A 和 B 一边一个
        if left_result and right_result:
            return root

        # 左子树有一个点或者左子树有LCA
        if left_result:
            return left_result

        # 右子树有一个点或者右子树有LCA
        if right_result:
            return right_result

        # 左右子树啥都没有
        return None


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

s = Solution()

print(s.lowestCommonAncestor(t1, t9, t12))
