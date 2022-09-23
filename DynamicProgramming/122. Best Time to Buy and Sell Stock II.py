class Solution:
    def maxProfit(self, prices):
        length = len(prices)

        dp = [[0, 0] for _ in range(length)]

        dp[0][0] = - prices[0]
        dp[0][1] = 0

        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])

        return dp[-1][1]

    def maxProfit_2(self, prices):
        length = len(prices)

        dp = [[0, 0] for _ in range(length)]

        dp[0][0] = - prices[0]
        dp[0][1] = 0

        for i in range(1, length):
            dp[i % 2][0] = max(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1] - prices[i])
            dp[i % 2][1] = max(dp[(i - 1) % 2][1], dp[(i - 1) % 2][0] + prices[i])

        return dp[(length - 1) % 2][1]

