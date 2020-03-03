class Solution(object):
    # O(m*n) space
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return

        row = len(dungeon)
        col = len(dungeon[0])

        dp = [[0 for x in range(col)] for x in range(row)]

        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])

        for j in range(col - 2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j + 1] - dungeon[-1][j])

        for i in range(row - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])

        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])

        return dp[0][0]

    # O(n) space
    def calculateMinimumHP_1(self, dungeon):
        if not dungeon:
            return

        r, c = len(dungeon), len(dungeon[0])
        dp = [0 for _ in range(c)]
        dp[-1] = max(1, 1 - dungeon[-1][-1])

        for i in range(c - 2, -1, -1):
            dp[i] = max(1, dp[i + 1] - dungeon[-1][i])

        for i in range(r - 2, -1, -1):
            dp[-1] = max(1, dp[-1] - dungeon[i][-1])
            for j in range(c - 2, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])
        return dp[0]



so = Solution()

print(so.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))

print(so.calculateMinimumHP_1([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
