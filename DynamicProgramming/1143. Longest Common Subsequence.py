class Solution:
    def longestCommonSubsequence(self, text1, text2):

        n = len(text1) + 1
        m = len(text2) + 1

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j]
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            # print(dp)
        return dp[-1][-1]
