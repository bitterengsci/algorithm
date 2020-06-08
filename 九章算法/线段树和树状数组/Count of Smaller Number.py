from BinaryIndexTree import *

class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    # Approach: Binary Search
    def countOfSmallerNumber_1(self, A, queries):
        A = sorted(A)
        
        results = []
        for q in queries:
            # binary search to find the first number in A >= q
            if len(A) == 0 or A[-1] < q:
                results.append(len(A))
                continue
            
            start, end = 0, len(A) - 1
            while start + 1 < end:
                mid = start + (end - start) // 2
                if A[mid] < q:
                    start = mid
                else:
                    end = mid
            if A[start] >= q:
                results.append(start)
            elif A[end] >= q:
                results.append(end)
            else:
                results.append(end + 1)
            
        return results


    # Approach: 先把两个数组排序, 再求解。比较麻烦的是要把排序前和排序后的queries对应起来
    def countOfSmallerNumber(self, A, queries):
        if not queries: return []
        if not A: return [0] * len(queries)
            
        A.sort()

        maps = {}
        for i in range(len(queries)):
            if queries[i] not in maps:
                maps[queries[i]] = [i]
            else:
                maps[queries[i]].append(i)
                
        res = [0] * len(queries)
        count = 0
        j = 0
        for n in sorted(maps.keys()):
            while j < len(A) and A[j] < n:
                count += 1
                j += 1
            for l in maps[n]:
                res[l] = count

        return res

######################################################
#          Binary Index Tree -- Jiuzhang Ans
######################################################
# 用binary indexed tree 来做这道题。
# 为了降低bit数组的尺寸， 求取了两个数组的最大值。
# 因为每个数组都允许为空，处理起来比较麻烦。 
# 如果直接按照data value < 10000, 可以直接生成 bit = BITree(10000), 浪费空间，但是code会简洁一些
def countOfSmallerNumber(self, A, queries):
        if not queries: return []
        if not A: return [0] * len(queries)
        
        A.sort()
        '''
        size = 0
        if len(A) > 0:
            size = max(size, A[-1])
            
        if len(queries) > 0:
            size = max(size, sorted(queries)[-1])
            
        bit = BinaryIndexTree(size + 1, update=False)   
        # 注意此处定义Bit有些不同, 不是用数组A, 而是用一个size
        '''
        bit = BinaryIndexTree(range(10000), update=False)
        
        result = []
        for a in A:
            bit.update(a, 1)
            
        for num in queries:
            result.append(bit.get_prefix_sum(num - 1))
        return result

######################################################
#          Segment Tree -- Jiuzhang Ans (Python 2)
######################################################
class Solution:
    class SegmentTreeNode:
        def __init__(self, start, end, count):
            self.start, self.end, self.count = start, end, count
            self.left, self.right = None, None
        
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # build segmeng tree
        root = self.build(0, 10000)
        result = []
        
        # modify count value for each
        for num in A:
            self.modify(root, num, 1)
        
        for i in queries:
            count = 0
            if i > 0:
                count = self.query(root, 0, i - 1)
            result.append(count)
        
        return result
    
    def build(self, start, end):
        if start >= end:
            return SegmentTreeNode(start, end, 0)
        root = SegmentTreeNode(start, end, 0)
        mid = start + (end - start) / 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        return root
    
    def modify(self, root, index, value):
        if root.start == index and root.end == index:
            root.count += value
            return
        # query
        mid = root.start + (root.end - root.start) / 2
        if index <= mid:
            self.modify(root.left, index, value)
        
        if mid < index:
            self.modify(root.right, index, value)
        root.count = root.left.count + root.right.count
    
    def query(self, root, start, end):
        if start == root.start and end == root.end:
            return root.count
        
        mid = root.start + (root.end - root.start) / 2
        if end <= mid:
            return self.query(root.left, start, end)
        
        if start > mid:
            return self.query(root.right, start, end)
            
        return self.query(root.left, start, mid) + \
            self.query(root.right, mid + 1, end)

######################################################
#       Something goes wrong with my code
######################################################
class SegmentTree(object):  # SegmentTreeNode
    def __init__(self, start, end, value=0):
        self.start, self.end = start, end   # index
        self.val = value      # val = sum/max/count, etc..
        self.left, self.right = None, None

    def build(self, start, end, array):
        if start > end:
            return None
    	
        if start == end: # a leaf node
            return SegmentTree(start, end, 0)

        node = SegmentTree(start, end, 0)

        mid = (start + end) // 2
        node.left = self.build(start, mid, array)
        node.right = self.build(mid + 1, end, array)

        node.val = node.left.val + node.right.val
        
        return node # the root

    def modify(self, root, index, value):
        if root is None:
            return
        
        if root.start == root.end == index:
            root.val = value
            return
    
        if root.left.end >= index:
            self.modify(root.left, index, value)
        else:
            self.modify(root.right, index, value)
        
        root.val = root.left.val + root.right.val

    def query(self, root, start, end):
        if root.start > end or root.end < start:
            return 0
    
        if start <= root.start and root.end <= end:
            return root.val
        
        return self.query(root.left, start, end) + self.query(root.right, start, end)

class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
        
    # Approach: Segment Tree, 
    # val = 'count' (occurences of numbers in this range)
    def countOfSmallerNumber(self, A, queries):
        if not A: return [0] * len(queries)
        
        minimum, maximum = min(A), max(A)
        segtree = SegmentTree(0, maximum - minimum, 0)
        root = segtree.build(0, maximum - minimum, list(range(minimum, maximum + 1)))
        
        # modify count value for each
        for num in A:
            idx = num - minimum
            segtree.modify(root, idx, 1)
            
        # results 
        results = []
        for i in queries:
            if  minimum <= i <= maximum and type(i) == int:
                idx = i - minimum
                results.append(segtree.query(root, 0, idx - 1))
            else:
                results.append(0)
        
        return results
