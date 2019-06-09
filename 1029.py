'''
1029. Two City Scheduling

There are 2N people a company is planning to interview.  The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.


'''
import operator
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        person = zip(*costs)
        diff = list(map(operator.sub,person[0],person[1]))
        diff_ref = list(map(list,zip(diff, person[0],person[1])))
        diff_ref.sort()
        mid = len(diff_ref)//2
        a = sum(list(map(list,zip(*diff_ref[:mid])))[1])
        b = sum(list(map(list,zip(*diff_ref[mid:])))[2])
        return(a+b)