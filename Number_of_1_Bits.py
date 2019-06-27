class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        for i in range(32):
            counter += (n & 1)
            n >>= 1
        return counter

n = b"00000000000000000000000000001011"
sol = Solution()
print(sol.hammingWeight(n))