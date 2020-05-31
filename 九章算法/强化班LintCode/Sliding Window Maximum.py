from collections import deque

class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        if not nums or not k: return []
            
        dq = deque([])   # save indices
        
        # initialization
        for i in range(k - 1):
            print(i, dq)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
        print("initialization", dq)
        
        # find result
        result = []
        for i in range(k - 1, len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            
            print("i=", i, dq)
            result.append(nums[dq[0]])
            # If current maximum is the leftmost one and
            # it will be move out of the window in the next step
            if dq[0] == i - k + 1:
                dq.popleft()
                
        return result