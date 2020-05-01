#-*-coding:utf-8-*-
'''
Description
Implement function atoi to convert a string to an integer.

If no valid conversion could be performed, a zero value is returned.
If the correct value is out of the range of representable values,
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Note
    库函数实现题目, 但考察的不是调用库函数吖..
    最大的int用(1 << 31) - 1 或者 sys.maxsize
    MaxInt = (1 << 31) - 1
    MaxInt = sys.maxsize

    INT_MAX = 2147483647      这种编程习惯不好!!!
'''
class Solution:
    """
    @param str: A string
    @return: An integer
    """

    def atoi(self, str):
        str = str.strip()

        if len(str) == 0:
            return 0

        # INT_MAX, INT_MIN = 2147483647, -2147483648
        INT_MAX = 2147483647        # 这种编程习惯不好!!!

        sign = 1
        i = 0

        if str[0] == '-':
            i += 1          # 不要用str = str[1:], 'str' is unsubscriptable-object
            sign = -1
        elif str[0] == "+":
            i += 1

        number = 0
        for i in range(i, len(str)):
            if str[i] == '.':
                break
            else:
                number = number * 10 + int(str[i])
                i += 1
        number *= sign
        if number > INT_MAX:
            return INT_MAX
        elif number < - INT_MAX - 1:
            return - INT_MAX - 1
        else:
            return number

    def myAtoi(self, str):
        str = str.strip()
        if str == "":
            return 0
        i = 0
        sign = 1
        ret = 0
        MaxInt = (1 << 31) - 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1

        for i in range(i, len(str)):
            if str[i] < '0' or str[i] > '9':
                break
            ret = ret * 10 + int(str[i])
            if ret > sys.maxsize:
                break

        ret *= sign
        if ret >= MaxInt:
            return MaxInt
        if ret < MaxInt * -1:
            return MaxInt * - 1 - 1
        return ret


s = Solution()
print(s.atoi("12214748364722.0"))
