import math
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res, last, n = 0, -1, len(seats)
        for i in range(n):
            if seats[i]:
                res = max(res, i if last < 0 else (i-last)/2)
                last = i

        return max(res, n-last- 1)

so = Solution()
print(so.maxDistToClosest([1,0,0,0,1,0,1]))
print(so.maxDistToClosest([1,0,0,0]))