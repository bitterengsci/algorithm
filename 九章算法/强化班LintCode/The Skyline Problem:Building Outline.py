# 此题不能用list来模拟heap (新插入一个元素时, heap的heapify时间复杂度O(logn), 但sort TC=O(nlogn), 会导致超时)

# 用HashHeap
class HashHeap:
    def __init__(self, desc=False):
        self.hash = dict()
        self.heap = []
        self.desc = desc
        
    @property
    def size(self):
        return len(self.heap)
        
    def push(self, item):
        self.heap.append(item)
        self.hash[item] = self.size - 1
        self._sift_up(self.size - 1)
        
    def pop(self):
        item = self.heap[0]
        self.remove(item)
        return item
    
    def top(self):
        return self.heap[0]
        
    def remove(self, item):
        if item not in self.hash:
            return
            
        index = self.hash[item]
        self._swap(index, self.size - 1)
        
        del self.hash[item]
        self.heap.pop()
        
        # in case of the removed item is the last item
        if index < self.size:
            self._sift_up(index)
            self._sift_down(index)

    def _smaller(self, left, right):
        return right < left if self.desc else left < right

    def _sift_up(self, index):
        while index != 0:
            parent = (index - 1) // 2
            if self._smaller(self.heap[parent], self.heap[index]):
                break
            self._swap(parent, index)
            index = parent
    
    def _sift_down(self, index):
        if index is None:
            return
        while index * 2 + 1 < self.size:
            smallest = index
            left = index * 2 + 1
            right = index * 2 + 2
            
            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left
                
            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right
                
            if smallest == index:
                break
            
            self._swap(index, smallest)
            index = smallest
        
    def _swap(self, i, j):
        elem1 = self.heap[i]
        elem2 = self.heap[j]
        self.heap[i] = elem2
        self.heap[j] = elem1
        self.hash[elem1] = j
        self.hash[elem2] = i


class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    # my ans (wrong)
    def buildingOutline(self, buildings):
        points = []
        for start, end, height in buildings:
            points.append([start, height, True])  # start
            points.append([end, height, False])   # end
            # OR use height for start, -height for end
        
        points.sort(key=lambda x: (x[0], x[2]))

        heights = HashHeap(desc=True)   # a max-heap
        intervals = []
        prev_pos = 0
        for pos, height, is_start in points:
            max_height = heights.top()[0] if heights.size else 0
            self.merge_to(intervals, prev_pos, pos, max_height)
            if is_start:
                heights.push(height)
            else:
                heights.remove(height)
            prev_pos = pos
        
        print(intervals)
        return intervals
        
    def merge_to(self, intervals, start, end, height):
        if start is None or height == 0 or start == end:
            return
        
        if not intervals:
            intervals.append([start, end, height])
            return
        
        _, prev_end, prev_height = intervals[-1]
        if prev_height == height and prev_end == start:
            intervals[-1][1] = end
            return
        
        intervals.append([start, end, height])


    # 九章算法答案
    def buildingOutline_jiuzhang(self, buildings):
        points = []
        for index, (start, end, height) in enumerate(buildings):
            points.append((start, height, index, True))
            points.append((end, height, index, False))
        points = sorted(points)
        
        maxheap = HashHeap(desc=True)
        intervals = []
        last_position = None
        for position, height, index, is_start in points:
            max_height = maxheap.top()[0] if maxheap.size else 0
            self.merge_to(intervals, last_position, position, max_height)
            if is_start:
                maxheap.push((height, index))
            else:
                maxheap.remove((height, index))
            last_position = position

        return intervals
        
    def merge_to(self, intervals, start, end, height):
        if start is None or height == 0 or start == end:
            return
        
        if not intervals:
            intervals.append([start, end, height])
            return
        
        _, prev_end, prev_height = intervals[-1]
        if prev_height == height and prev_end == start:
            intervals[-1][1] = end
            return
        
        intervals.append([start, end, height])
