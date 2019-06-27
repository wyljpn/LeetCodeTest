class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycle = set()
        while n != 1 and n not in cycle:
            cycle.add(n)
            n = sum(int(i) ** 2 for i in str(n))

        print(cycle)
        return n == 1

sol = Solution()
res = sol.isHappy(19)
print(res)