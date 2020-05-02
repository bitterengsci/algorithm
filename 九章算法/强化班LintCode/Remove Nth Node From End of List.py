    # one pass solution 快慢指针 (my ans)
    '''
    problem:
        Last executed input
        [1]
        1
    AttributeError: 'NoneType' object has no attribute 'next'
        while fast.next:
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        fast = head
        slow = head
        i = 0
        
        # 快指针先走n步
        while fast and i < n:
            fast = fast.next
            i += 1
            
        # 慢指针开始走
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return head
    
    # 九章算法答案
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        tmp = res
        for i in range(n):
            head = head.next
            
        while head:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        return res.next