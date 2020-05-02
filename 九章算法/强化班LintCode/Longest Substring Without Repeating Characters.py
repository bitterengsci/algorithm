    # Approach: 同向双指针
    def lengthOfLongestSubstring(self, s):
        len_string = 0
        freq = [0] * 26
        j = 0
        
        for i in range(len(s)):
            while j < len(s) and not freq[ord(s[j]) - ord('a')]:
                freq[ord(s[j])- ord('a')] = 1
                j += 1
            len_string = max(len_string, j - i)
            
            freq[ord(s[i]) - ord('a')] = 0
            
        return len_string
    
    # 九章算法答案
    def lengthOfLongestSubstring(self, s):
        unique_chars = set([])
        j = 0
        longest = 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in unique_chars:
                unique_chars.add(s[j])
                j += 1
            longest = max(longest, j - i)
            unique_chars.remove(s[i])
            
        return longest

