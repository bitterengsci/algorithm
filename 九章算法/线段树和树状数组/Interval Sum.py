"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class SegmentTree(object):  # SegmentTreeNode
    def __init__(self, start, end, sum=0):   # val = sum or max, etc..
        self.start = start    # index
        self.end = end        # index
        self.sum = sum
        self.left, self.right = None, None

    @classmethod
    def build(self, start, end, array):
        if start > end:
            return None
    	
        if start == end: # a leaf node
            return SegmentTree(start, end, array[start])

        node = SegmentTree(start, end, array[start])

        mid = (start + end) // 2
        node.left = self.build(start, mid, array)
        node.right = self.build(mid + 1, end, array)
        # lsum, rsum = 0, 0
        # if node.left:
        #     lsum += node.left.sum
        # if node.right:
        #     rsum += node.right.sum
        # node.sum = lsum + rsum
        node.sum = node.left.sum + node.right.sum
        
        return node # the root

    @classmethod
    def modify(cls, root, index, value):
        if root is None:
            return

        if root.start == root.end:
            root.sum = value
            return
    
        if root.left.end >= index:
            cls.modify(root.left, index, value)
        else:
            cls.modify(root.right, index, value)
        
        root.sum = root.left.sum + root.right.sum

    @classmethod
    def query(cls, root, start, end):
        if root.start > end or root.end < start:
            return 0
    
        if start <= root.start and root.end <= end:   # why <= not ==?
            return root.sum
        
        return cls.query(root.left, start, end) + cls.query(root.right, start, end)


class Solution:
    """
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """
    
    # Approach: cumulative sum array
    def intervalSum_1(self, A, queries):
        cumulative = [0]
        
        for i in A:
            cumulative.append(cumulative[-1] + i)
        
        res = []
        for q in queries:
            res.append(cumulative[q.end + 1] - cumulative[q.start])
        
        return res
        
    # Approach: Segment Tree
    def intervalSum(self, A, queries):
        
        root = SegmentTree.build(0, len(A)-1, A)
        res = []
        for q in queries:
            res.append(SegmentTree.query(root, q.start, q.end))
            
        return res