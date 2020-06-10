class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
        # INT_RANGE = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & 0xffffffff, (a & b) <<1
        return a