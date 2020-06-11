"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        print(len(hashTable))
        
        capacity = 2 * len(hashTable)   # double the capacity
        
        new_hashT = [None] * capacity
        
        for pos in hashTable:
            head = pos
            while head:
                # rehashing
                idx = head.val % capacity
                if new_hashT[idx] is None:
                    new_hashT[idx] = ListNode(head.val)
                else:
                    newhead = new_hashT[idx]
                    while newhead.next:
                        newhead = newhead.next
                    newhead.next = ListNode(head.val)
                
                head = head.next
        
        return new_hashT