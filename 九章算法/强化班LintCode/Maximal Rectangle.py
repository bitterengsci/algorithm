class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        max_rect = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            # for index, num in enumerate(row):
            #     heights[index] = heights[index] + 1 if num else 0
            heights = [heights[i] + 1 if row[i] else 0 for i in range(len(matrix[0]))]
            max_rect = max(max_rect, self.largestRectangleArea(heights))
            
        return max_rect
    
    
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