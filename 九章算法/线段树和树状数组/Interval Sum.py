"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from SegmentTree import *
from BinaryIndexTree import *

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
        for q in queries: # 需要注意的是 prefixsum中元素下标 和 原数组中元素下标的不同
            res.append(cumulative[q.end + 1] - cumulative[q.start])
        
        return res
        
    # Approach: Segment Tree
    def intervalSum_2(self, A, queries):
        root = SegmentTree.build(0, len(A)-1, A)
        res = []
        for q in queries:
            res.append(SegmentTree.query(root, q.start, q.end))
            
        return res

    # Approach: Binary Index Tree
    def intervalSum(self, A, queries):
        bitree = BinaryIndexTree(A)
        
        res = []
        for q in queries:
            res.append(bitree.get_prefix_sum(q.end) - bitree.get_prefix_sum(q.start - 1))
            
        return res