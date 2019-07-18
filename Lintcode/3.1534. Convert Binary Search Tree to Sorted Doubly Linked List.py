#-*-coding:utf-8-*-
'''
Description
    Convert a BST to a sorted circular doubly-linked list in-place.
    Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.


    We want to transform this BST into a circular doubly linked list.
    Each node in a doubly linked list has a predecessor and successor.
    For a circular doubly linked list, the predecessor of the first element is the last element,
    and the successor of the last element is the first element.

    The figure below shows the circular doubly linked list for the BST above.
    The "head" symbol means the node it points to is the smallest element of the linked list.

    Specifically, we want to do the transformation in place. After the transformation,
    the left pointer of the tree node should point to its predecessor,
    and the right pointer should point to its successor.
    We should return the pointer to the first element of the linked list.

    The figure below shows the transformed BST.
    The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def treeToDoublyList(self, root):
        if not root:
            return root

        first, last, prev = None, None, None

        # iterate the tree like a list
        for v in self.inorder(root):
            if first is None:
                first = v
                last = v
            if prev is not None:
                prev.right = v
                v.left = prev
            prev = v

        first.left = last
        last.right = first

        return first

    def inorder(self, node):
        if not node: return
        for n in self.inorder(node.left):
            yield n
        yield node
        for n in self.inorder(node.right):
            yield n


'''
    if node.left is leaf:
        node.left.right = node
    
    if node.right is leaf:
        node.right.right = node.ascentor
        node.ascentor.left = node.right
        node.right.left = node
        
    TODO 不知道如何实现 
'''
