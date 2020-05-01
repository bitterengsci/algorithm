#-*-coding:utf-8-*-
'''
Given a string(Given in the way of char array) and an offset,
rotate the string by offset in place. (rotate from left to right)

Challenge
    Rotate in-place with O(1) extra memory.
'''
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        length = len(s)
        if length > 0:
            offset = offset % len(s)    # 普通assignment 比 augmented assignment (offset %= length) 快, 不知道为什么...

        temp = (s + s)[length - offset: 2 * length - offset]

        for i in range(length):
            s[i] = temp[i]

    def rotateString2(self, s, offset):
        return s[offset+1:] + s[:offset+1]

s = Solution()
print(s.rotateString2('abcdef', 3))
print(s.rotateString2("abcdefg", 3))    # "efgabcd"
