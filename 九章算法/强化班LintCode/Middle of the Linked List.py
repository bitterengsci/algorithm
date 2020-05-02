    # 快慢指针
    def middleNode(self, head: ListNode) -> ListNode:
        # we only have one node in the LL
        # if head.next is None:
        #     return head
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # one middle node
        if fast.next:
            return slow.next
        # two middle nodes
        return slow