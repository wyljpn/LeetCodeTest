class Solution:
    def countSubstrings(self, s):

        n = len(s)

        # dp数组意义
        # dp[i:j+1]是否为回文
        dp = [[False for _ in range(n)] for _ in range(n)]

        result = 0

        # 因为dp[i][j]的状态要依赖左下方dp[i+1][j-1]的状态
        # 遍历的顺序要从下到上，从做到右。
        # j的顺序是从i开始到末尾
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        result += 1
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                        result += 1

        # print(dp)

        return result