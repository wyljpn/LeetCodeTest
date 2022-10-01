class Solution:
    def numDistinct(self, s, t):

        n = len(s) + 1
        m = len(t) + 1

        # dp数组的意义
        # 以s[i]为后缀的字符串中，以t[j]为后缀的字符串出现的次数
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # 初始化
        # 删除以s[i]为后缀的字符串的字符后可以变成空字符串，方式只有一种。
        for i in range(n):
            dp[i][0] = 1
        # s空字符串没有办法变成t[j]，所以dp[0][:]为0

        for i in range(1, n):
            for j in range(1, m):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                # 不想等时，删除掉s[i-1]
                else:
                    dp[i][j] = dp[i - 1][j]

        # print(dp)

        return dp[-1][-1]