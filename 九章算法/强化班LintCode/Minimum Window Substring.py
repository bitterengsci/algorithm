'''
最短子串

C: 集齐B中字母种类, 阈值处理
同向双指针, 记录每个字符ch在两个指针中间出现的次数freq[ch]
如果ch在T中出现w次, 一旦freq[ch]增加到w, 记录这个字符被完成了
如果ch要从区间中一走, freq[ch]减少到w-1, 记录这个字符没被完成

完成的字符数=T中不同字符数 -> 当前区间包含组成T的所有字符
'''
    # Approach: 同向双指针 (我的答案, 不对...)
    def minWindow(self, s: str, t: str) -> str:
        ans = None
        num_complete_chars = 0
        
        freqT = {}
        for i in t:
            if i in freqT:
                freqT[i] += 1
            else:
                freqT[i] = 1
                
        freq = {}
        
        j = 0
        for i in range(len(s)):
            print("i", i, j)
            while j < len(s):
                print(i, j)
                if s[j] in freq:
                    freq[s[j]] += 1
                else:
                    freq[s[j]] = 1
                
                if s[j] in freqT and freq[s[j]] == freqT[s[j]]:
                    num_complete_chars += 1
                
                if num_complete_chars == len(freqT):
                    if ans is None or len(s[i:j+1]) < len(ans):
                        ans = s[i:j+1]
                    break
                j += 1
            freq[s[i]] -= 1
            if s[i] in freqT:
                num_complete_chars -= 1
        return ans
            
            
    # 九章算法答案
    # dict.get(key, default_value)
    def minWindow(self, s, t):
        if s is None:
            return ""
        
        freqT = {}
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1
            
        target_unique_chars = len(freqT)
        matched_unique_chars = 0
        
        freq = {}
        j = 0
        min_len = len(s) + 1
        ans = ""
        
        for i in range(len(s)):
            while j < len(s) and matched_unique_chars < target_unique_chars:
                if s[j] in freqT:
                    freq[s[j]] = freq.get(s[j], 0) + 1
                    if freq[s[j]] == freqT[s[j]]:
                        matched_unique_chars += 1
                j += 1
                
            if j - i < min_len and matched_unique_chars == target_unique_chars:
                min_len = j - i
                ans = s[i:j]
                
            if s[i] in freqT:
                if freq[s[i]] == freqT[s[i]]:
                    matched_unique_chars -= 1
                freq[s[i]] -= 1
        return ans