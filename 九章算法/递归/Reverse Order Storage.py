class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: n
    @return: A list of reversed elements
    """

    # Approach: Recursion
    def reverseStore(self, head):
        if head is None:
            return []
        if head.next is None:
            return [head.val]

        return self.reverseStore(head.next) + [head.val]

l = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
print(Solution().reverseStore(l))

