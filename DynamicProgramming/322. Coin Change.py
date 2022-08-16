class Solution(object):
    # 动态规划：自下而上[通过]
    # 我们采用自下而上的方式进行思考。仍定义 F(i)F(i) 为组成金额 ii 所需最少的硬币数量，假设在计算 F(i)F(i) 之前，我们已经计算出 F(0)-F(i-1)F(0)−F(i−1) 的答案。

    def coinChange(self, coins, amount):
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # dp[i - coin] + 1. 加1枚指定coin的意思。
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] != float('inf'):
            return dp[-1]
        else:
            return -1

    def coinChange_1(self, coins, amount):
        import functools
        @functools.lru_cache(None)
        def helper(amount):
            if amount ==0:
                return 0
            return min(helper(amount-c) if amount-c>=0 else float('inf') for c in coins) + 1

        res = helper(amount)
        return res if res != float('inf') else -1


so = Solution()

print(so.coinChange([1,2,5], 11))