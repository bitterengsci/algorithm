#-*-coding:utf-8-*-
'''
Description
    Given a root of Binary Search Tree with unique value for each node.
    Remove the node with given value.
    If there is no such a node with given value in the binary search tree, do nothing.
    You should keep the tree still a binary search tree after removal.
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# 九章算法答案 (太brute force了吧 醉了)
class Solution_not_good:
    """
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    ans = []

    def inorder(self, root, value):
        if root is None:
            return

        self.inorder(root.left, value)
        if root.val != value:
            self.ans.append(root.val)
        self.inorder(root.right, value)

    def build(self, l, r):
        if l == r:
            node = TreeNode(self.ans[l])
            return node

        if l > r:
            return None

        mid = (l + r) / 2
        node = TreeNode(self.ans[mid])
        node.left = self.build(l, mid - 1)
        node.right = self.build(mid + 1, r)
        return node

    def removeNode(self, root, value):
        # write your code here
        self.inorder(root, value)
        return self.build(0, len(self.ans) - 1)


# 我的答案

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        # root is None, do nothing
        if not root:
            return root

        # root.val equals value
        if root.val == value:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # root.left is not None and root.right is not None
            # replace the root with max node on the left (which I stick to)
            #               or the min node on the right

            if root.left.right is None:
                right_subtree = root.right
                root = root.left
                root.right = right_subtree
                return root

            else:
                replaced_node_root = self.find_left_max(root.left)
                left_subtree = root.left
                right_subtree = root.right
                root = replaced_node_root.right
                replaced_node_root.right = replaced_node_root.right.left

                root.left = left_subtree
                root.right = right_subtree
                return root

        if root.val > value:
            root.left = self.removeNode(root.left, value)

        if root.val < value:
            root.right = self.removeNode(root.right, value)

        return root


    def find_left_max(self, root):
        right_subtree = root.right
        if not right_subtree.right and not right_subtree.left:
            return root


root = TreeNode(5)
n3 = TreeNode(3)
n2 = TreeNode(2)
n4 = TreeNode(4)
n6 = TreeNode(6)
n3.left = n2
n3.right = n4
n2.left = TreeNode(1)
root.left = n3
root.right = n6

s = Solution()
# new_root = s.removeNode(n3, 6)
# print(new_root.val)
# print(new_root.left.val)
# print(new_root.right.val)


new_root = s.removeNode(root, 3)
print(new_root.val)
print(new_root.left.val)
# print(new_root.val)
# print(new_root.val)
