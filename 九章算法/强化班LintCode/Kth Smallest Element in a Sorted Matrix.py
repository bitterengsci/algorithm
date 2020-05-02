    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        
        visited = [[False] * C for _ in range(R)] 
        # 切记不能用 visited = [[False] * C] * R, 否则各行一样
        
        minheap = [(0, 0, matrix[0][0])]
        while k > 1:
            curr = minheap.pop(0)
            
            # 右边的
            if curr[0] <= R - 2 and not visited[curr[0] + 1][curr[1]]:
                minheap.append((curr[0] + 1, curr[1], matrix[curr[0] + 1][curr[1]]))
                visited[curr[0] + 1][curr[1]] = True
                
            # 下边的
            if curr[1] <= C - 2 and not visited[curr[0]][curr[1] + 1]:
                minheap.append((curr[0], curr[1] + 1, matrix[curr[0]][curr[1] + 1]))
                visited[curr[0]][curr[1] + 1] = True
            
            # sort a list of tuples
            minheap = sorted(minheap, key=lambda tup: tup[2])
            k -= 1
        
        return minheap[0][2]
    
    
    # Approach: 二分答案