#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (44.90%)
# Likes:    4313
# Dislikes: 158
# Total Accepted:    570.8K
# Total Submissions: 1.3M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# Example 2:
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3

# @lc code=start
class Solution:
    def numIslands(self, grid):
        islands = 0
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    self.part_of_island(i, j, grid)
        return islands

    def part_of_island(self, i, j, grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0'
        self.part_of_island(i, j+1, grid)
        self.part_of_island(i, j-1, grid)
        self.part_of_island(i+1, j, grid)
        self.part_of_island(i-1, j, grid)  


# @lc code=end

'''
* zip() can only permute two lists with equal length.
* DFS considers the call stacks into space complexity

* Time complexity: O(M×N) where M is the number of rows and N is the number of columns.
* Space complexity : worst case O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.
'''