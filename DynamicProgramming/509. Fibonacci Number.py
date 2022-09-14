class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        
        dp = [0] * (n + 1)
        
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]


    def fib_2(self, n):

        if n < 2:
            return n

        dp = [0 for _ in range(n + 1)]

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


    def fib_3(self, n):

        if n < 2:
            return n

        dp = [0, 1]

        for _ in range(2, n + 1):
            dp[1], dp[0] = dp[0] + dp[1], dp[1]

        return dp[-1]

