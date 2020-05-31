class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        
        
        start, end = 0, x
        
        while start + 1 < end:
            
            mid = start + (end - start) // 2
            
            if mid ** 2 >= x:
                end = mid
            else:
                start = mid
                
        
        if end ** 2 > x:
            return start
            
        return end
