#-*-coding:utf-8-*-
'''
Description
    Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        if not root:
            return []

        left = self.searchRange(root.left, k1, k2)
        right = self.searchRange(root.right, k1, k2)

        if root.val > k2:
            return left

        if root.val < k1:
            return right

        return left + [root.val] + right


'''
考点：
二叉查找树 ：
    二叉排序树或者是一棵空树，或者是具有下列性质的二叉树：
    （1）若左子树不空，则左子树上所有结点的值均小于它的根结点的值；
    （2）若右子树不空，则右子树上所有结点的值均大于或等于它的根结点的值；
    （3）左、右子树也分别为二叉排序树；
题解：从给定的BST的根节点开始查找，如果位于[k1,k2]，存入结果，向左右子树分别搜索。
'''
class Solution2:
    def searchRange2(self, root, k1, k2):
        ans = []
        if root is None:
            return ans
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                if k2 >= queue[index].val >= k1:
                    ans.append(queue[index].val)

                queue.append(queue[index].left)
                queue.append(queue[index].right)

            index += 1
        return sorted(ans)
