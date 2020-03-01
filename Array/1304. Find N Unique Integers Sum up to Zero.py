class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        if n % 2 == 1:
            arr += [0]

        for i in range(1, int(n / 2) + 1):
            arr += [i, -i]
        return arr

    def sumZero_1(self, n):
        return range(1 - n, n, 2)


so = Solution()

print(so.sumZero(5))
print(so.sumZero(3))
print(so.sumZero(1))
