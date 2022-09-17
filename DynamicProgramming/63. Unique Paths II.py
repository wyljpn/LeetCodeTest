class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            if not obstacleGrid[0][j]:
                dp[0][j] = 1
            else:
                break

        for i in range(m):
            if not obstacleGrid[i][0]:
                dp[i][0] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


so = Solution()

print(so.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
