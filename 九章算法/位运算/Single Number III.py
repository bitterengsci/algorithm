class Solution:
    """
    @param A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        # 用于记录, 区分“两个”数组
        diff = 0
        for num in A:
            diff ^= num
        
        # 原码, 就是其二进制表示（注意, 有一位符号位）
        # 反码, 正数的反码就是原码, 负数的反码是符号位不变, 其余位取反
        # 补码, 正数的补码就是原码, 负数的补码是反码+1
        # 在机器中都是采用补码形式存
        
        # 取最后一位1, diff & (-diff)就是取diff的最后一位1的位置
        diff &= -diff
        
        rets = [0, 0]
        for i in A:
            # 分属两个“不同”的数组
            if i & diff == 0:
                rets[0] ^= i
            else:
                rets[1] ^= i

        return rets