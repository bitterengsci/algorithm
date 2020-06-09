'''
* 调用: 需要反转 [31, 0]
* 终止条件: if(pos == 31) {return n;}
* 拆解: 需要反转 [31, pos] 之间的位

long last = n & 1; // 取最后一位
long ret reverseBits(n >> 1, pos + 1); // 右移一位
ret += last << (31 - pos);  // 左移(31-pos)位

111..01  last=1
111..0   ret=0..111
return 1(第31-pos位)111..0

'''

class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def reverseBits(self, n):
        return self.recursion(n, 0)  # 调用:需要反转 [31, 0]

    def recursion(self, n, pos):
        if pos == 31:   # 终止条件
            return n
        # 拆解: 需要反转 [31, pos]之间的位
        last = n & 1        # 取最后一位
        ret = self.recursion(n >> 1, pos + 1)  # 右移一位
        ret += last << (31 - pos)       # 左移(31-pos)位
        return ret