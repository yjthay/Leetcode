'''
64. Minimum Path Sum
Medium

1363

39

Favorite

Share
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

import copy
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        min_sum = copy.deepcopy(grid)
        rows = len(grid)-1
        cols = len(grid[0])-1
        for row in range(rows,-1,-1):
            for col in range(cols,-1,-1):
                if row == rows and col == cols:
                    min_sum[row][col]=grid[row][col]
                elif row==rows:
                    min_sum[row][col] = min_sum[row][col+1]+min_sum[row][col]
                elif col==cols:
                    min_sum[row][col] = min_sum[row+1][col]+min_sum[row][col]
                else:
                    min_sum[row][col] = min(min_sum[row+1][col], min_sum[row][col+1])+min_sum[row][col]
        return min_sum[0][0]