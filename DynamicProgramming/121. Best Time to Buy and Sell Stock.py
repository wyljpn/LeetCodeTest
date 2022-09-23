class Solution:
    def maxProfit(self, prices):

        length = len(prices)

        if length == 1:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(length)]

        dp[0][0] = - prices[0]
        dp[0][1] = 0

        # dp[i][0] 表示第i天持有股票所得现金。取前天股票的价格和当天股票价格的最低值。（因为取反了，所以是用max）
        # dp[i][1] 表示第i天不持有股票所得最多现金。比较卖出股票之后的盈利，取max。
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

        return dp[-1][1]


    def maxProfit_2(self, prices):

        length = len(prices)

        if length == 1:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(length)]

        dp[0][0] = prices[0]
        dp[0][1] = 0

        # dp[i][0] 表示第i天持有股票所得现金。取前天股票的价格和当天股票价格的最小值。没有取反，所以直接用min
        # dp[i][1] 表示第i天不持有股票所得最多现金。比较卖出股票之后的盈利，取max。
        for i in range(1, length):
            dp[i][0] = min(dp[i - 1][0], prices[i])
            dp[i][1] = max(dp[i - 1][1], prices[i] - dp[i - 1][0])

        return dp[-1][1]

    def maxProfit_3(self, prices):
        length = len(prices)

        if length == 1:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(2)]

        dp[0][0] = prices[0]
        dp[0][1] = 0

        for i in range(1, length):
            dp[i % 2][0] = min(dp[(i - 1) % 2][0], prices[i])
            dp[i % 2][1] = max(dp[(i - 1) % 2][1], prices[i] - dp[(i - 1) % 2][0])

        return dp[(length - 1) % 2][1]

