#-*-coding:utf-8-*-
'''
Description
    Given a string, find the length of the longest substring without repeating characters.

Note
    同向双指针
'''
class Solution:
    """
    @param s: a string
    @return: an integer
    """

    # def lengthOfLongestSubstring(self, s):
    #     element = list()
    #     i = 0
    #     while i < len(s):
    #         if s[i] in element:
    #             break
    #         element.append(s[i])
    #         i += 1

    #     return i

    def lengthOfLongestSubstring(self, s):
        print('String =', s)
        j = 0
        unique_chars = set([])
        n = len(s)
        longest = 0
        for i in range(n):
            print('i =', i, 'j =', j)
            while j < n and s[j] not in unique_chars:
                unique_chars.add(s[j])
                j += 1
            longest = max(longest, j - i)
            unique_chars.remove(s[i])

        return longest

s = Solution()
print(s.lengthOfLongestSubstring("aab"))
