class Solution:
    def isSubsequence(self, s, t):

        n = len(t) + 1
        m = len(s) + 1

        # dp数组的意义
        # 在t[:i+1]中s[:j+1]出现的次数
        # 可以通过dp[-1][-1]==len(s)判断是否是子序列
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # 初始化
        # 初始值都为0就好

        for i in range(1, n):
            for j in range(1, m):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # print(dp)

        return dp[-1][-1] == len(s)

