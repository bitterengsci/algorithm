class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings1(self, s):
        if not s:  # "" -> 0
            return 0
        dp = [0] * (len(s) + 1)
        
        dp[0] = 1  # empty string to empty string
        
        if int(s[0]) != 0:
            dp[1] = 1
        
        if len(s) == 1:
            return dp[1]
        
        for i in range(2, len(s) + 1):
            
            # one digit s[i-1]
            if int(s[i-1]) != 0:
                dp[i] += dp[i-1]
            
            # two digit s[i-2: i]
            if 26 >= int(s[i-2: i]) >= 10:
                 dp[i] += dp[i-2]
                 
        return dp[-1]
        
    # Approach: sliding array
    def numDecodings(self, s):
        if not s:  # "" -> 0
            return 0
        dp = [0] * 2
        
        dp[0] = 1  # empty string to empty string
        
        if int(s[0]) != 0:
            dp[1] = 1
        
        if len(s) == 1:
            return dp[1]

        now = 0
        for i in range(2, len(s) + 1):
            # two digit s[i-2: i]
            if not (26 >= int(s[i-2: i]) >= 10):
                dp[now] = 0
            # one digit s[i-1]
            if int(s[i-1]) != 0:
                dp[now] += dp[1-now]
            
            now = 1 - now
                 
        return dp[1-now]