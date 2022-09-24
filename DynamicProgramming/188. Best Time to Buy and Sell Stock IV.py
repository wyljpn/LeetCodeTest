class Solution:
    def maxProfit(self, k, prices):

        n = len(prices)

        # 下标为单数时记录买入
        # 下标为偶数时记录卖出
        dp = [[0 for _ in range(k * 2 + 1)] for _ in range(n)]

        for j in range(1, 2 * k, 2):
            dp[0][j] = - prices[0]
        # print(dp)

        for i in range(1, n):
            for j in range(1, 2 * k + 1):
                if j % 2 == 1:
                    # 买入
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                else:
                    # 卖出
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
            # print(dp)

        return dp[-1][-1]
