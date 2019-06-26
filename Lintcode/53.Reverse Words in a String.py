#-*-coding:utf-8-*-
'''
Description
    Given an input string, reverse the string word by word.

Clarification
    What constitutes a word?
    A sequence of non-space characters constitutes a word and some words have punctuation at the end.
    Could the input string contain leading or trailing spaces?
    Yes. However, your reversed string should not contain leading or trailing spaces.
    How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.
'''
class Solution:
    """
    @param: s: A string
    @return: A string
    """

    # def reverseWords(self, s):
    #     s = s.strip()
    #     if len(s) == 0:
    #         return ''
    #     words = s.split()
    #     s_reversed = str()
    #     for i in reversed(words):
    #         s_reversed += str(i) + ' '

    #     return s_reversed.strip()

    def reverseWords(self, s):
        # strip()去掉s头尾的空格，split()按照空格分割字符串，reversed翻转，''.join按照空格连接字符串
        return ' '.join(reversed(s.strip().split()))
