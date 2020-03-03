class Solution(object):
    # Bottom up
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
