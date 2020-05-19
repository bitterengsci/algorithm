class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    '''
    dp[stone]为set，记录青蛙可以跳的距离。
    状态转移方程为:
        * 跳k - 1到stone + k - 1: dp[stone + k - 1].add(k - 1)
        * 跳k到stone + k: dp[stone + k].add(k)
        * 跳k + 1到stone + k + 1: dp[stone + k + 1].add(k + 1)
    '''
    def canCross(self, stones):
        dp = {0: set([0])} # dp[stone]为set, 记录青蛙跳到stone时, 可能跳的距离
        for stone in stones[1:]:
            dp[stone] = set()

        for stone in stones:
            for k in dp[stone]:
                # k - 1
                if k - 1 > 0 and stone + k - 1 in dp:
                    dp[stone + k - 1].add(k - 1)
                # k
                if stone + k in dp:
                    dp[stone + k].add(k)
                # k + 1
                if stone + k + 1 in dp:
                    dp[stone + k + 1].add(k + 1)
    
        print(dp)
        return len(dp[stones[-1]]) > 0