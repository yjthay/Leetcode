'''
63. Unique Paths II
Medium

862

120

Favorite

Share
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.
'''
import copy


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        paths = copy.deepcopy(obstacleGrid)
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    paths[row][col] = 0
                else:
                    if row == 0 and col == 0:
                        paths[row][col] = 1
                    elif row == 0:
                        paths[row][col] = paths[row][col - 1]
                    elif col == 0:
                        paths[row][col] = paths[row - 1][col]
                    else:
                        paths[row][col] = paths[row - 1][col] + paths[row][col - 1]
                        # if obstacleGrid[row-1][col]==1:
                        #     paths[row][col] = paths[row][col-1]
                        # elif obstacleGrid[row][col-1]==1:
                        #     paths[row][col] = paths[row-1][col]
                        # else:
                        #     paths[row][col] = paths[row-1][col]+paths[row][col-1]
        # print(paths)
        return paths[rows - 1][cols - 1]
