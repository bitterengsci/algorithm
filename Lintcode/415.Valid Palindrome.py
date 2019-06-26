#-*-coding:utf-8-*-
'''
Description
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Challenge
    O(n) time without extra memory


Note
    use s[start].isalpha() to test whether it is a 字母~ ~

'''
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    # def isPalindrome(self, s):
    #     if len(s) == 0:
    #         return True
    #
    #     start = 0
    #     end = len(s) - 1
    #     while start < end:
    #         while s[start].lower() < 'a' or s[start].lower() > 'z':
    #             start += 1
    #         while s[end].lower() < 'a' or s[end].lower() > 'z':
    #             end -= 1
    #
    #         if start < end and s[start].lower() != s[end].lower():
    #             # print(s[start], s[end])
    #             return False
    #         start += 1
    #         end -= 1
    #
    #     return True

    def isPalindrome(self, s):
        start, end = 0, len(s) - 1

        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                # print(s[start], s[end])
                return False
            start += 1
            end -= 1

        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("ab"))
