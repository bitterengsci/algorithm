class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param i: A bit position
    @param j: A bit position
    @return: An integer
    """
    def updateBits(self, n, m, i, j):
        # Java
        # ((~((((-1) << (31 - j)) >>> (31 - j + i)) << i)) & n) | (m << i)
        tmp = ((~((((-1) << (31 - j) & 0xFFFFFFFF) >> (31 - j + i)) << i)) & 0xFFFFFFFF) & n | ((m << i) & 0xFFFFFFFF)
        
        if tmp & (1 << 31):
            return tmp ^ ~(0xFFFFFFFF)
            
        return tmp
