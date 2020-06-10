class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    # One-pass, constant extra space    
    def singleNumberII(self, A):
        once, twice = 0, 0
        
        for num in A:
            once = (once ^ num) & (~twice)
            twice = (twice ^ num) & (~once)

        return once