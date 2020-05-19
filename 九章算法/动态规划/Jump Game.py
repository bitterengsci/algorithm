class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump_wrong(self, A):
        if A == [0]: return True
        dp = [False] * len(A)
        
        dp[0] = A[0] > 0
        
        for i in range(1, len(A)):
            for j in range(1, A[i]):
                dp[i] = any([dp[j-i] and dp[j] <= i-j for j in range(1, A[i]) if i-j >=0])
        
        print(dp)
        return dp[-1]
        
    def canJump_jiuzhang(self, A):
        curr_pos = 0
        jump_farest = 0
        for step_forward in A[:-1]:
            print(step_forward, curr_pos, jump_farest)
            jump_farest = max(jump_farest, curr_pos + step_forward)
            if(jump_farest <= curr_pos):
                return False
            curr_pos += 1
        return True

    def canJump(self, A):
        jump_farest = 0
        for pos in range(len(A) - 1):
            print(A[pos], pos, jump_farest)
            jump_farest = max(jump_farest, pos + A[pos])
            if(jump_farest <= pos):
                return False
        return True


Solution().canJump([2, 3, 1, 1, 4])