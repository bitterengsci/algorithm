class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        return self.countOnes(a ^ b)
    
    def countOnes(self, num):
        count = 0
        bound = 2 ** 32 - 1
        while num != 0 and num > -bound:
            num = num & (num - 1)
            count += 1
        return count