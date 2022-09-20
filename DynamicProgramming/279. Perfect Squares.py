class Solution:
    def numSquares(self, n):

        dp = [float("inf") for i in range(n + 1)]

        dp[0] = 0

        for i in range(1, n + 1):
            perfect_square = i * i
            if perfect_square > n:
                break

            for j in range(perfect_square, n + 1):
                dp[j] = min(dp[j], dp[j - perfect_square] + 1)

        return dp[-1]