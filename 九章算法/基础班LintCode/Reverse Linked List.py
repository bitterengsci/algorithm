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
        
        prev = None
        
        while head:
            #temp记录下一个节点，head是当前节点
            tmp = head.next
            head.next = prev
            prev, head = head, tmp
        
        return prev
