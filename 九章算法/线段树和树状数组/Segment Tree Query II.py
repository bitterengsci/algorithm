"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The count number in the interval [start, end]
    """
    def query(self, root, start, end):
        if not root or root.start > end or root.end < start:
            return 0
        
        if start <= root.start and root.end <= end:
            return root.count
            
        return self.query(root.left, start, end) + self.query(root.right, start, end)