    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longest_len = 0
        freq = {}
        
        j = 0
        for i in range(len(s)): # 主指针
            while j < len(s) and len(freq) <= 2: # 副指针
                freq[s[j]] = freq.get(s[j], 0) + 1
                j += 1
                
                if len(freq) <= 2:  # 满足条件更新最优解
                    longest_len = max(longest_len, j-i)
            
            # increment i, 处理i在freq里
            if s[i] in freq:
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    del freq[s[i]]
            
        return longest_len