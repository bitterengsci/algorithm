"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        if start > end:
            return
        
        mid = (start + end) // 2

        root = SegmentTreeNode(start, end)
        if start == end:
            return root
        root.left = self.build(start, mid)
        root.right = self.build(mid+1, end)
        
        return root