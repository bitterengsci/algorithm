class BinaryIndexTree(object):
    def __init__(self, A, update=True): # build the tree
        self.nums = A
        self.size = len(A)
        self.bit = [0 for _ in range(self.size + 1)]  # 树状数组的下标从 1 开始计数
        
        if update:
            for i, num in enumerate(self.nums):
                self.update(i, num)   # # 树状数组的下标从 1 开始计数

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