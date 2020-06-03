class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minstack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        if self.stack and number > self.minstack[-1]:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(number)
        self.stack.append(number)
        
        # print(self.stack, self.minstack)

    """
    @return: An integer
    """
    def pop(self):
        self.minstack.pop(-1)
        return self.stack.pop(-1)

    """
    @return: An integer
    """
    def min(self):
        return self.minstack[-1]
