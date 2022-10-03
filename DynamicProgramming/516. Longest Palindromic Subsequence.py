class Solution:
    def longestPalindromeSubseq(self, s):

        n = len(s)

        # dp数组意义
        # s[i:j+1]中最长回文子序列的长度
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # 
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]