'''
70. Climbing Stairs
Easy

2217

81

Favorite

Share
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''
class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n-1 == 0:
        #     return 1
        # elif n-2 ==0:
        #     return 2
        # else:
        #     return self.climbStairs(n-1)+self.climbStairs(n-2)
        master=[]
        for i in range(n):
            if i==0:
                master.append(1)
            elif i==1:
                master.append(2)
            else:
                master.append(master[i-2]+master[i-1])
        return master[-1]