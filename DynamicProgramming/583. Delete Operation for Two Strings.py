class Solution:
    def minDistance(self, word1, word2):

        n = len(word1) + 1
        m = len(word2) + 1

        # dp数组的意义
        # 要使word1[:i]和word2[:j]相等，所需要删除的字符的数量
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # 初始化
        # 把word1[:i]中的字符都删掉，就能拿到一个空字符串
        for i in range(n):
            dp[i][0] = i

        # 把word1[:i]中的字符都删掉，就能拿到一个空字符串
        for j in range(m):
            dp[0][j] = j

        for i in range(1, n):
            for j in range(1, m):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1

        # print(dp)

        return dp[-1][-1]