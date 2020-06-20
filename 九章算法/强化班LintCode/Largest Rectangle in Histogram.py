class MonoStack():

    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    # 新元素插入前, pop掉所有比它大的
    def append(self, a, strict):
        return self.push(a, strict)

    def push(self, a, strict=False):
        popped_nums = []
        i = len(self.stack) - 1
        while i >= 0:
            if self.stack[i] > a:
                popped_nums.append(self.stack.pop())
                i -= 1
            elif self.stack[i] == a and strict:
                popped_nums.append(self.stack.pop())
                i -= 1
            else:
                break
        self.stack.append(a)
        return popped_nums  # values popped, for pushing a into the stack

# Wrong...
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        if not height:
            return 0
        max_area = height[0]
        
        monostack = MonoStack()
        
        for i in height + [-1]:
            pops = monostack.append(i, True)
            if pops:
                max_area = max(max_area, len(pops) * min(pops))
        return max_area

Solution().largestRectangleArea([2,1,5,6,2,3])



"""
维护一个单调递增栈，逐个将元素 push 到栈里。
push 进去之前先把 >= 自己的元素 pop 出来。 
每次从栈中 pop 出一个数的时候，就找到了往左数比它小的第一个数（当前栈顶）和往右数比它小的第一个数（即将入栈的数）， 
从而可以计算出这两个数中间的部分宽度 * 被pop出的数，就是以这个被pop出来的数为最低的那个直方向两边展开的最大矩阵面积。 
因为要计算两个数中间的宽度，因此放在 stack 里的是每个数的下标。
"""
# Jiuzhang Ans
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        
        for index, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= height: #如果列表尾部高度大于当前高度
                popped_index = stack.pop()
                left_index = stack[-1] if stack else -1	
                #列表为空则宽度为index，否则为index-indices_stack[-1]-1
                width = index - left_index - 1 
                max_area = max(max_area, width * heights[popped_index])
                
            stack.append(index)		#压入列表中
            
        return max_area