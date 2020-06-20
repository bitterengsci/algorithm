# 把所有字符一个个放到 stack 里， 如果碰到了 ]，就从 stack 找到对应的字符串和重复次数，decode 之后再放回 stack 里


"""
Given an expression s contains numbers, letters and brackets. 
Number represents the number of repetitions inside the brackets(can be a string or another expression)．
Please expand expression to be a string.
"""

class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):

        self.stack = []
        
        i = 0
        while i < len(s):
            if s[i].isdigit():      # digit
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                self.stack.append(int(s[i:j]))
                i = j - 1
            elif s[i] == ']':
                string = ''
                while self.stack:
                    w = self.stack.pop(-1)
                    if w == '[':
                        break
                    string = w + string
                times = self.stack.pop(-1)
                for _ in range(times):
                    self.stack.append(string)
            else:
                self.stack.append(s[i])   # pure letter or "["
            i += 1
            
        return ''.join(self.stack)