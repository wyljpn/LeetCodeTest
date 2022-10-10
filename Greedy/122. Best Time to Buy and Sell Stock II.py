class Solution:
    # 贪心
    # 把利润的计算分解成每天。
    # 为每天都计算卖出的利润。同时记住今日的价格，可以计算明日卖出的利润。
    def maxProfit(self, prices):
        
        res = 0
        prePrice = prices[0]
        
        for price in prices:
            profit = price - prePrice
            
            if profit > 0:
                res += profit
                
            prePrice = price
        
        return res
   
    # 动态规划
    def maxProfit(self, prices):
        
        # dp数组的意义
        # index=0的值代表购买股票的价格（取反）
        # index=1的值代表卖出股票后的现金
        dp = [[0, 0] for _ in range(len(prices))]
        
        dp[0][0] -= prices[0]
        
        for i in range(1, len(prices)):
            # （昨日不买，今日买进入股票的价格）和（昨日买入价格）的最小值。（因为是负数，所以用max）
            dp[i][0] = max(dp[i-1][1] - prices[i], dp[i-1][0])
            # （昨日买入，今日卖出的收益）和（昨日不买的价格）
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
        
        return max(dp[-1])
