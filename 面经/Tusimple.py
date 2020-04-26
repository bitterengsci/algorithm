# check if two given line segments intersect
# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
def two_line_intersect():
    pass

# proper fraction 分母不超过N的从小到大真分数序列


# 一个4*4的棋盘，O代表空位，X或者Y代表棋子
# 每次可以移动一步，最少多少次可以移动至存在排成一列/行/斜线的X或者Y

# 两堆石子(m,n) 两个人A和B 每次只能取(0, k)或(k, 0)或(k, k) 其中k<=min(m, n)
# 谁先把两堆石子都取完谁赢。如果A先取，A有没有必胜策略
# 威佐夫博弈，可以O(1)做

# 矩阵里有两个岛，求连接两个岛的最短路径

# 矩阵里有多少个形状不同的岛屿

# 一个整型数组（有正有负），从左边和右边分别连续地取一些元素，求取走的值的和最大可能是多少



#
def reconstruction(upper, lower, colsum):
    if not colsum:
        return [[], []]
    ans = [[None] * len(colsum) for _ in range(2)] 
    
    uppersum, lowersum = 0, 0
    
    # colsum = 0 or 2
    for i, val in enumerate(colsum):
        if val == 0:
            ans[0][i], ans[1][i] = 0, 0
        if val == 2:
            ans[0][i], ans[1][i] = 1, 1
            uppersum += 1
            lowersum += 1
            
    # colsum == 1 
    for i, val in enumerate(colsum):
        if val == 1:
            if uppersum < upper:
                ans[0][i], ans[1][i] = 1, 0
                uppersum += 1
            elif lowersum < lower:
                ans[0][i], ans[1][i] = 0, 1
                lowersum += 1
    for i in range(2):
        for j in reversed(range(len(colsum))):
            if ans[i][j] is None:
                return [[], []] # no valid ans
    if uppersum != upper or lowersum != lower:
        return [[], []]
    return ans
                
#print(reconstruction(2, 1, []))       
#print(reconstruction(2, 1, [1, 1, 1]))
#print(reconstruction(2, 1, [1, 1, 2]))
#print(reconstruction(2, 2, [2, 0, 2]))
print(reconstruction(4, 7, [2, 1, 2, 2, 1, 1, 1]))

#
def visit_index(arr, start):
    if not arr or start >= len(arr):
        return False
    # we may have a valid ans
    return dfs(arr, start, [False] * len(arr))

def dfs(arr, start, visited):
    # termination of dfs
    if arr[start] == 0:
        return True
    # dfs
    valid = False
    if 0 <= start + arr[start] < len(arr):
       if not visited[start + arr[start]]:
           visited[start + arr[start]] = True
           valid = dfs(arr, start + arr[start], visited)
    if 0 <= start - arr[start] < len(arr):
       if not visited[start - arr[start]]:
           visited[start - arr[start]] = True
           valid = valid or dfs(arr, start - arr[start], visited)
    return valid

# print(visit_index([], 5))
print(visit_index([3, 1, 0, 1, 2], 2))

if __name__ == "__main__":
    pass