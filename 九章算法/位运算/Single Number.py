class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber1(self, A):
        num = A[0]
        
        for i in A[1:]:
            num ^= i
            
        return num
           
    def singleNumber(self, A):
        num = 0
        
        for i in A:
            num ^= i
            
        return num