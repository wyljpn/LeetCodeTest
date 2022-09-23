class Solution:
    def maxProfit(self, prices):
        n = len(prices)

        # 0: 买入状态
        # 1: 保持卖出股票状态
        # 2: 今天卖出状态
        # 3: 冷却状态
        dp = [[0 for _ in range(4)] for _ in range(n)]

        dp[0][0] = - prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][1], dp[i - 1][3]) - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2])
            dp[i][2] = dp[i - 1][0] + prices[i]
            dp[i][3] = dp[i - 1][2]

        return max(dp[-1][1], dp[-1][2], dp[-1][3])