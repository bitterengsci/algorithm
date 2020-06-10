class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    # check lowbit
    def checkPowerOf2(self, n):
        if n <= 0: 
            return False 
        
        n = n & (n - 1)
        
        return n == 0