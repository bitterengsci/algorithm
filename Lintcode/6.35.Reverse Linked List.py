#-*-coding:utf-8-*-
'''
Description
    Reverse a linked list.
'''
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        prev = None  # prev表示前继节点

        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev
