import heapq

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    
    # 用 maxheap 保存左半部分的数，用 minheap 保存右半部分的数
    # 把所有的数一左一右的加入到每个部分。左边部分最大的数就一直都是 median
    # 这个过程中，可能会出现左边部分并不完全都 <= 右边部分的情况
    # 这种情况发生的时候，交换左边最大和右边最小的数即可
    def medianII(self, nums):
        self.minheap, self.maxheap = [], []
        medians = []
        for num in nums:
            self.add(num)
            medians.append(self.median)
        return medians
    
    @property
    def median(self):
        return -self.maxheap[0]

    def add(self, value):
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -value)
        else:
            heapq.heappush(self.minheap, value)
            
        if len(self.minheap) == 0 or len(self.maxheap) == 0:
            return

        if -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))