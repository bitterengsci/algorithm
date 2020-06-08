"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        if root.start > end or root.end < start:
            return -float('inf')   # return -0x7fffff
        
        if root.start >= start and root.end <= end:
            return root.max
            
        return max(self.query(root.left, start, end), self.query(root.right, start, end))