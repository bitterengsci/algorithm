from SegmentTree import *
from BinaryIndexTree import *

# Approach: Segment Tree 线段树
class Solution:
    """
    @param: A: An integer array
    """
    def __init__(self, A):
        self.root = SegmentTree.build(0, len(A) - 1, A)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        return SegmentTree.query(self.root, start, end)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        SegmentTree.modify(self.root, index, value)


# Approach: Binary Index Tree 树状数组
class Solution2:
    """
    @param: A: An integer array
    """
    def __init__(self, A):
        self.array = A
        self.bitree = BinaryIndexTree(A)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        return self.bitree.get_prefix_sum(end) - self.bitree.get_prefix_sum(start - 1) 

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        self.bitree.update(index, -self.array[index])
        self.array[index] = value
        self.bitree.update(index, value)