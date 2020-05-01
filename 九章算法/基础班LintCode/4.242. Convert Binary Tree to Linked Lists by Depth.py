#-*-coding:utf-8-*-
'''
Description
    Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
    (e.g., if you have a tree with depth D, you'll have D linked lists).
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        result = []
        if root is None:
            return result

        queue = [root]

        while queue:

            ll = ListNode(queue[0].val)
            i = 1
            l_pointer = ll
            while i < len(queue):
                l_pointer.next = ListNode(queue[i].val)
                l_pointer = l_pointer.next
                i += 1
            result.append(ll)

            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level

        return result
