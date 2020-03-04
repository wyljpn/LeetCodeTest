class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        # dp = [[0] * len(obstacleGrid[0])] * len(obstacleGrid)
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else:
                break

        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    continue

        return dp[-1][-1]


so = Solution()

print(so.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
