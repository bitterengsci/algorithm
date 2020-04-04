#-*-coding:utf-8-*-
'''
Description
    Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.
    If the given node has no in-order successor in the tree, return null.
    It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)

Challenge
    O(h), where h is the height of the BST.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        if not root:
            return

        if root.val > p.val:
            if root.left.val == p.val:
                if not root.left.right:
                    return root
                else:
                    return self.findmin(root.left.right)
            else:
                successor = self.inorderSuccessor(root.left, p)
                if not successor:
                    return root
                else:
                    return successor

        if root.val < p.val:
            return self.inorderSuccessor(root.right, p)

        if root.val == p.val:
            return self.findmin(root.right)

    def findmin(self, root):
        if not root:
            return root
        if root.left is None:
            return root
        return self.findmin(root.left)

'''
九章算法答案
    
首先要确定中序遍历的后继:
    如果该节点有右子节点, 那么后继是其右子节点的子树中最左端的节点
    如果该节点没有右子节点, 那么后继是离它最近的祖先, 该节点在这个祖先的左子树内.
    
使用循环实现:
    查找该节点, 并在该过程中维护上述性质的祖先节点
    查找到后, 如果该节点有右子节点, 则后继在其右子树内; 否则后继就是维护的那个祖先节点
    
使用递归实现:
    如果根节点小于或等于要查找的节点, 直接进入右子树递归
    如果根节点大于要查找的节点, 则暂存左子树递归查找的结果, 如果是 null, 则直接返回当前根节点; 反之返回左子树递归查找的结果.
    在递归实现中, 暂存左子树递归查找的结果就相当于循环实现中维护的祖先节点.
'''
class Solution2:
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)

        left = self.inorderSuccessor(root.left, p)
        if left != None:
            return left
        else:
            return root
