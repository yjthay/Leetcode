'''
72. Edit Distance
Hard

2101

30

Favorite

Share
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)+1
        len2 = len(word2)+1
        grid = [[0 for col in range(len2)] for row in range(len1)]
        for row in range(len1):
            for col in range(len2):
                if row==0 and col == 0:
                    grid[row][col] = 0
                elif row==0:
                    grid[row][col] = grid[row][col-1]+1
                elif col==0:
                    grid[row][col] = grid[row-1][col]+1
                else:
                    if word1[row-1]!=word2[col-1]:
                        grid[row][col] = min(grid[row-1][col-1],grid[row][col-1],grid[row-1][col])+1
                    elif word1[row-1]==word2[col-1]:
                        grid[row][col] = grid[row-1][col-1]
        #print(grid)
        return grid[len1-1][len2-1]