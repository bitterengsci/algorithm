class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    - 情况一: 最后一个字符翻译成字母 S[i-1]
        - S[i-1] ='0' 不能翻译成字母
        - S[i-1] ∈ {'1', ..., '9'} 1种方式翻译成一个字母, 共f[i-1]种方式 
        - S[i-1] = '*' 9种可能翻译成一个字母, 共 9 * f[i-1]种方式
    - 情况二:最后两个字符翻译成字母 S[i-2]S[i-1]
        - S[i-2] = '0' 不能翻译成字母
        - S[i-2] = '1'
            S[i-1] ∈ {'0', ..., '9'} 1种可能翻译成一个字母, 共f[i-2]种方式
            S[i-1] = '*' 9种可能翻译成一个字母, 共 9 * f[i-2]种方式
        - S[i-2] = '2'
            S[i-1] ∈ {'0', ..., '6'} 1种可能翻译成一个字母, 共f[i-2]种方式
            S[i-1] ∈ {'7', ..., '9'} 不能翻译成字母
            S[i-1] = '*' 6种可能翻译成一个字母, 共 6 * f[i-2]种方式
        - S[i-2] ∈ {'3', ..., '9'} 不能翻译成字母
        - S[i-2] = '*'
            S[i-1] ∈ {'0', ..., '6'} 2种可能翻译成一个字母, 共 2 * f[i-2]种方式
            S[i-1] ∈ {'7', ..., '9'} 1种可能翻译成一个字母, 共 f[i-2]种方式
            S[i-1] = '*' 15种可能翻译成一个字母, 共 15 * f[i-2]种方式
    """
    def numDecodings(self, s):
        if not s:  # "" -> 0
            return 0
        dp = [0] * (len(s) + 1)
        
        dp[0] = 1  # empty string to empty string
        
        if s[0] == "*":
            dp[1] = 9
        elif int(s[0]) != 0:
            dp[1] = 1
        
        if len(s) == 1:
            return dp[1]
            
        mod = 1000000007
        
        for i in range(2, len(s) + 1):
            # one digit s[i-1]
            if s[i-1] == "*":
                dp[i] = (dp[i] + 9 * dp[i-1]) % mod
            elif int(s[i-1]) != 0:  # 1 ~ 9
                dp[i] = (dp[i] + dp[i-1]) % mod
            
            # two digit s[i-2: i]
            if s[i-2] == "*":
                if s[i-1] == "*":
                    dp[i] = (dp[i] + 15 * dp[i-2]) % mod
                elif 6 >= int(s[i-1]) >= 0:  # 0 ~ 6
                    dp[i] = (dp[i] + 2 * dp[i-2]) % mod
                else: # 7 ~ 9
                    dp[i] = (dp[i] + dp[i-2]) % mod
                    
            elif s[i-2] == "1":
                if s[i-1] == "*":
                    dp[i] = (dp[i] + 9 * dp[i-2]) % mod
                else: # 0 ~ 9
                    dp[i] = (dp[i] + dp[i-2]) % mod
            
            elif s[i-2] == "2":
                if s[i-1] == "*":
                    dp[i] = (dp[i] + 6 * dp[i-2]) % mod
                elif 6 >= int(s[i-1]) >= 0:  # 0 ~ 6
                    dp[i] = (dp[i] + dp[i-2]) % mod
 
        return dp[-1]