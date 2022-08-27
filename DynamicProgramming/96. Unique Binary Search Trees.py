class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0 for _ in range(n + 1)]

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # 因为要计算的是左子树从0到i-1和右子树从i-1到0的组合，所以j范围是(1, i+1)
                dp[i] += dp[j - 1] * dp[i - j]
                # i=2: dp[0]*dp[1] + dp[1]*dp[0]
                # i=3: dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0]

        return dp[-1]

