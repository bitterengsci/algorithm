class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    # Approach: o(m)时间复杂度
    # python3数值超过int后自动转long, 所以要自己bound一下
    def countOnes1(self, num):
        count = 0
        bound = 2 ** 32 - 1
        while num != 0 and num > -bound:
            num = num & (num - 1)
            count += 1
        return count
        
    # Approach: 不用lower bound的方法, 而是先变负为正
    # 注意, mask 要放在前面
    def countOnes(self, num):
        mask = 2**32 - 1 
        
        if num < 0:
            num = mask & num 
            
        count = 0
        while num:
            count += 1 
            num &= (num - 1)
            
        return count