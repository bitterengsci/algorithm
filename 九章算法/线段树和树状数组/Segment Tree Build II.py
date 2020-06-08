"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, A):
        return self.buildtree(0, len(A) - 1, A)
        
    def buildtree(self, start, end, A):
        
        if start > end:
            return
        
        if start == end:
            return SegmentTreeNode(start, end, A[start])
            
        mid = (start + end) // 2
        left = self.buildtree(start, mid, A)
        right = self.buildtree(mid + 1, end, A)
        
        root = SegmentTreeNode(start, end, max(left.max, right.max))
        root.left, root.right = left, right
        
        return root