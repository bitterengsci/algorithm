'''
Implement double sqrt(double x) and x >= 0, compute and return the square root of x
'''
class Solution:
    """
    @param: x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        if x >= 1:
            start, end = 1, x
        else:
            start, end = x, 1
        
        while end - start > 1e-10:
            mid = (start + end) / 2
            if mid ** 2 < x:
                start = mid
            else:
                end = mid
                
        return start