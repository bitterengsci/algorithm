class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString_wrong(self, s, offset):
        
        def reverse(s):
            for i in range(len(s)//2):
                s[i], s[-1-i] = s[-1-i], s[i]
        
        # 3 step reverse
        
        # step 1. reverse all
        reverse(s)
        print(s)
        
        # step 2. reverse s[:offset]
        reverse(s[:offset])   # wrong, pass a copy of s[:offset] to the func
        print(s)
        
        # step 3. reverse s[offset:]
        reverse(s[offset:])   # wrong, pass a copy of s[offset:] to the func
        print(s)
    
    def rotateString(self, s, offset):
        if not s: return s
        
        offset %= len(s)
        # 3 step reverse
        
        # step 1. reverse all
        for i in range(len(s)//2):
            s[i], s[-1-i] = s[-1-i], s[i]
        print(s)
        
        # step 2. reverse s[:offset]
        for i in range(offset//2):
            s[i], s[offset -1 - i] = s[offset -1 - i], s[i]
        print(s)
        
        # step 3. reverse s[offset:]
        for i in range((len(s) - offset) // 2):
            s[offset + i], s[-1 - i] = s[-1 - i], s[offset + i]
        print(s)
        
    