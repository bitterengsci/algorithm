'''
    Naive Method (Time Limit Exceeded)
'''
class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lfu = {}
        self.time = 0

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key not in self.cache and len(self.cache) >= self.capacity:
            least_used_key = min(self.lfu, key=lambda k: (self.lfu[k][0], self.lfu[k][1]))
            self.cache.pop(least_used_key)
            self.lfu.pop(least_used_key)
        
        self.cache[key] = value
        self.lfu[key] = [self.lfu[key][0] + 1, self.time] if key in self.lfu else [1, self.time]
        self.time += 1

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key in self.cache:
            self.lfu[key] = [self.lfu[key][0] + 1, self.time]
            self.time += 1
            return self.cache[key]
        return -1


