#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.86%)
# Likes:    7270
# Dislikes: 1886
# Total Accepted:    1.3M
# Total Submissions: 3.8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        result = root
        carry = 0
        while l1 or l2 or carry:
            val1  = l1.val if l1 else 0
            val2  = l2.val if l2 else 0

            # carry, out = divmod(val1+val2 + carry, 10)  
            out = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
                        
            result.next = ListNode(out)
            result = result.next                      
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return root.next
        
# @lc code=end

