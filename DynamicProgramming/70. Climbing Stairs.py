class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
            
        # print(dp)
        
        return dp[-1]

    # 可以被当成是完全背包问题。每次走1步、2步当成是物品。也可以支持更多的步数。
    def climbStairs_2(self, n: int) -> int:

        dp = [0 for _ in range(n + 1)]

        dp[0] = 1

        nums = [1, 2]

        for i in range(1, n + 1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]

        return dp[-1]