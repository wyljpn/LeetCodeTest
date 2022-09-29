class Solution:
    def longestCommonSubsequence(self, text1, text2):

        n = len(text1) + 1
        m = len(text2) + 1

        # dp数组的意义
        # 长度为[0, i-1]的字符串text1与长度为[0, j-1]的字符串text2的最长公共子序列为dp[i][j]
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # 初始化
        # 初始状态都是0。
        # 当text1[0]==text2[0]的时候，dp[1][1]=0+1=1

        for i in range(1, n):
            for j in range(1, m):
                # 当相等的时候，+1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 当不等的时候，赋值为max(左边，上边)
                # 例如：比较abc和ace最后一个时，左边abc-ac=2，上边ab-ace=1. max(左边，上边)=2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        # print(dp)
        return dp[-1][-1]

