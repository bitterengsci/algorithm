class Solution:
    """
    @param: x: An integer
    @return: An integer
    """
    def swapOddEvenBits(self, x):
        # 1010 1010 1010 1010 1010 1010 1010 1010
        # Get all even bits of x 
        even_bits = x & 0xAAAAAAAA
        
        # 0101 0101 0101 0101 0101 0101 0101 0101
        # Get all odd bits of x 
        odd_bits = x & 0x55555555
          
        # Right shift even bits  
        # 刪除符号位运算（如果是>>的話, 负数还是负数, 要看題目要求而定）
        even_bits = even_bits >> 1
              
        # Left shift odd bits 
        odd_bits = odd_bits << 1
              
        # Combine even and odd bits 
        return even_bits | odd_bits
        
        # return ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1)