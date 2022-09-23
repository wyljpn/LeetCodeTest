class Solution:
    def maxProfit(self, prices):
        n = len(prices)

        # 0: 没有操作
        # 1: 第一次买入
        # 2: 第一次卖出
        # 3: 第二次买入
        # 4: 第二次卖出
        dp = [[0 for _ in range(5)] for _ in range(n)]

        dp[0][1] = - prices[0]
        dp[0][3] = - prices[0]  # 相当于第0天第一次买入了，第一次卖出了，然后在买入一次（第二次买入）

        for i in range(1, n):
            dp[i][1] = max(dp[i - 1][1], - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

        return dp[-1][4]