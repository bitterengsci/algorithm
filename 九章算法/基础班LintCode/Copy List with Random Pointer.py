# Solution 1 (line 13): TC=O(N)
# Solution 2 (line 86): TC=O(1)

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    
    # Approach: 利用hash map 来建立映射关系, node -> new node 然后，再copy所有node的next以及random指针
    
    # Approach: my ans
    # create next first, save each node in a hashmap using its label as the key
    # create random
    # TC=O(n), SC=O(n)
    def copyRandomList1(self, head):
        if head is None: return None
            
        mapping = {}
        new_head = RandomListNode(0)  # dummy node
        p, q = head, new_head
        
        while p:
            q.next = RandomListNode(p.label)
            p = p.next
            q = q.next
            mapping[q.label] = q
        
        p, q = head, new_head.next
        while q:
            if p.random:  # p.random is not None
                q.random = mapping[p.random.label]
            p = p.next
            q = q.next
        
        return new_head.next
    
    
    # 看不懂
    # O(1) space
    # step1: copy node
    # step2: copy random link
    # step3: split two lists
    # 没有使用HashMap，首先把clone node链接到原有链表，再拷贝random节点引用
    def copyRandomList2(self, head):
        if head is None: return None
        if head.next is None: return RandomListNode(head.label)
        
        # Copy Next
        dummy = RandomListNode(0)
        dummy.next = head
        while head:
            h = RandomListNode(head.label)
            h.next = head.next
            head.next = h
            head = head.next.next
        head = dummy.next
        
        # Copy Random
        dummy = RandomListNode(0)
        dummy.next = head
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next
        head = dummy.next
        
        # Split two lists
        dummy = RandomListNode(0)
        dummy.next = head.next
        h = dummy.next
        while h and h.next:
            tmp = h.next.next
            h.next = tmp
            h = h.next
            
        return dummy.next
        
    '''
    Leetcode explanation SUPER GOOD
    Approach 3: Iterative with O(1) Space
    
    1. Traverse the original list and clone the nodes as you go and place the cloned copy next to its original node. This new linked list is essentially a interweaving of original and cloned nodes.

        As you can see we just use the value of original node to create the cloned copy. The next pointer is used to create the weaving. Note that this operation ends up modifying the original linked list.
        cloned_node.next = original_node.next
        original_node.next = cloned_node

    2. Iterate the list having both the new and old nodes intertwined with each other and use the original nodes' random pointers to assign references to random pointers for cloned nodes. (If B has a random pointer to A, this means B' has a random pointer to A')

    3. Now that the random pointers are assigned to the correct node, the next pointers need to be correctly assigned to unweave the current linked list and get back the original list and the cloned list.
    '''
    def copyRandomList(self, head):
        if not head: return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        
        # Step 1: Clone node
        while ptr:
            # Cloned node
            new_node = RandomListNode(ptr.label)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Step 2: link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers, to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Step 3: Unweave the linked list to get back the original linked list and the cloned list.
        # A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head         # A->B->C
        ptr_new_list = head.next    # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old