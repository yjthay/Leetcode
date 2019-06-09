'''
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # if m==1 or n==1:
        #     return 1
        # else:
        #     return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        array = [[0 for col in range(m)] for row in range(n)]
        for row in range(n):
            for col in range(m):
                if row == 0 or col == 0:
                    # print(row,col)
                    array[row][col] = 1
                else:
                    array[row][col] = array[row - 1][col] + array[row][col - 1]
        return array[n - 1][m - 1]

