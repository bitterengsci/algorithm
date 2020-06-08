'''
Give you an integer array (index from 0 to n-1, where n is the size of this array, data value from 0 to 10000) . 
For each element Ai in the array, 
count the number of element before this element Ai is smaller than it and return count number array.

Example 1:
Input:
[1,2,7,8,5]
Output:
[0,1,2,3,2]

Example 2:
Input:
[7,8,2,1,3]
Output:
[0,1,0,0,2]

'''

########################################################################
#
#                           Segment Tree
#
########################################################################
class SegTree:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.count = 0
        if start != end:
            self.left = SegTree(start, (start + end) / 2)
            self.right = SegTree((start + end) / 2 + 1, end)
    
    def sum(self, start, end):
        if start <= self.start and end >= self.end:
            return self.count
        
        if self.start == self.end:
            return 0
        
        if end <= self.left.end:
            return self.left.sum(start, end)
        
        if start >= self.right.start:
            return self.right.sum(start, end)
        
        return (self.left.sum(start, self.left.end) + 
                self.right.sum(self.right.start, end))
    
    def inc(self, index):
        if self.start == self.end:
            self.count += 1
            return
        
        if index <= self.left.end:
            self.left.inc(index)
        else:
            self.right.inc(index)
        
        self.count = self.left.count + self.right.count


class Solution:
    """
    @param A: A list of integer
    @return: Count the number of element before this element 'ai' is 
             smaller than it and return count number list
    """
    def countOfSmallerNumberII(self, A):
        if len(A) == 0:
            return []
            
        root = SegTree(0, max(A))
        
        results = []
        for a in A:
            results.append(root.sum(0, a - 1))
            root.inc(a)
        return results


########################################################################
#
#                           Binary Index Tree (my ans)
#
########################################################################
class BinaryIndexTree(object):
    def __init__(self, A): # build the tree
        self.nums = A
        self.size = len(A)
        self.bit = [0 for _ in range(self.size + 1)]  # 树状数组的下标从 1 开始计数
        
        # for i, num in enumerate(self.nums):
        #     self.update(i, num)   # # 树状数组的下标从 1 开始计数

    def update(self, index, delta):
        i = index + 1
        while i <= self.size:
            self.bit[i] += delta
            i += self.lowbit(i)
    
    def lowbit(self, num):
        return num & (- num)
    
    def get_prefix_sum(self, index):
        i = index + 1
        presum = 0
        
        while i > 0:
            presum += self.bit[i]
            i -= self.lowbit(i)
        
        return presum

class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        if not A: return []
        bitree = BinaryIndexTree(list(range(max(A))))
        
        results = []
        for i in A:
            results.append(bitree.get_prefix_sum(i - 1))
            bitree.update(i, 1)
    
        return results

########################################################################
#
#               Fenwick Tree (Binary Indexed Tree) jiuzhang
#
########################################################################
class BITree(object):
    def __init__(self, range):
        self.bit = [0] * (range + 1)

    def increase(self, index, delta):
        i = index + 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += self.lowbit(i)
    
    def getPrefixSum(self, index):
        sum = 0
        i = index + 1
        while i >= 1:
            sum += self.bit[i]
            i -= self.lowbit(i)
        return sum
    
    def lowbit(self, x):
        return x & (-x)

class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        bitree = BITree(10000)
        
        results = []
        for i in A:
            results.append(bitree.getPrefixSum(i - 1))
            bitree.increase(i, 1)
            # print(bitree.bit)
    
        return results


########################################################################
#
#                使用块状数组实现分块检索  jiuzhang
#
########################################################################
# 时间复杂度 O(n * sqrt(size))
# 如果数值范围是 size，那么创建 sqrt(size) 个 sqrt(size) 大小的区间
# 每个区间记录总共有多少数，和不同的数出现几次
class Block:
    def __init__(self):
        self.total = 0
        self.counter = {}
        
class BlockArray:
    def __init__(self, max_value):
        self.blocks = [Block() for _ in range(max_value // 100 + 1)]
    
    def count_smaller(self, value):
        count = 0
        block_index = value // 100
        for i in range(block_index):
            count += self.blocks[i].total
        
        counter = self.blocks[block_index].counter
        for val in counter:
            if val < value:
                count += counter[val]
        return count
        
    def insert(self, value):
        block_index = value // 100
        block = self.blocks[block_index]
        block.total += 1
        block.counter[value] = block.counter.get(value, 0) + 1

class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        if not A:
            return []

        block_array = BlockArray(10000)
        results = []
        for a in A:
            count = block_array.count_smaller(a)
            results.append(count)
            block_array.insert(a)
        return results