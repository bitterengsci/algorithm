'''
* 42. Trapping Rain Water (1D)
* 407. Trapping Rain Water II (2D)

'''
# Approach 1: Brute Force TC=O(n^2), SC=O(1)
# For each element in the array, 
# we find the maximum level of water it can trap after the rain, 
# which is equal to the minimum of maximum height of bars on both the sides 
# minus its own height.

# Approach 2: Dynamic Programming TC=O(n), SC=O(n)
# 1.Find maximum height of bar from the left end upto an index i in the array left_max
# 2. Find maximum height of bar from the right end upto an index i in the array right_max
# 3. Iterate over the height array and update ans:
#       Add min(left_max[i], right_max[i]) - height[i] to ans
def trap(self, height: List[int]) -> int:
    if len(height) == 0:
        return 0
    
    left_max = [height[0]]
    for i in range(1, len(height)):
        left_max.append(max(height[i], left_max[i - 1]))
    
    right_max = [0] * len(height)
    right_max[-1] = height[-1]
    for i in range(len(height) - 2, 0, -1):
        right_max[i] = max(height[i], right_max[i + 1])
    
    ans = 0
    for i in range(1, len(height) - 1):
        ans += min(left_max[i], right_max[i]) - height[i]
        
    return ans