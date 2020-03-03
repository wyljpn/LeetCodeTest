class Solution(object):
    # O(n * m)
    def uniquePaths(self, m, n):
        if m <= 0 or n <= 0:
            return 0

        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]

    # O(n)
    def uniquePaths_1(self, m, n):
        if m <= 0 or n <= 0:
            return 0

        dp = [0 for j in range(n)]

        for j in range(n):
            dp[j] = 1

        for i in range(1, m):
            dp[0] = 1

            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]

        return dp[n-1]

so = Solution()

print(so.uniquePaths(3, 2))
print(so.uniquePaths_1(3, 2))
