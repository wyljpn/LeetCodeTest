class Solution(object):

    def minDistance(self, word1, word2):

        m, n = len(word1), len(word2)

        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果 word1[i] 与 word2[j] 相等。第 i 个字符对应下标是 i-1
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]


    def minDistance_1(self, word1, word2):

        m, n = len(word1), len(word2)

        dp = [0 for j in range(n + 1)]
        pre = 0

        for j in range(1, n + 1):
            dp[j] = j

        for i in range(1, m+1):
            temp = dp[0]
            dp[0] = i
            for j in range(1, n+1):
                pre = temp
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j - 1], dp[j], pre) + 1

        return dp[-1]

    def minDistance_2(self, word1, word2):

        n = len(word1) + 1
        m = len(word2) + 1

        # dp数组的意义
        # 要使word1[:i]和word2[:j]相等，所需操作的字符的数量
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # 初始化
        # 把word1[:i]中的字符都删掉，就能拿到一个空字符串，即与删掉出所有字符的word2相等
        for i in range(n):
            dp[i][0] = i

        # 把word1[:i]中的字符都删掉，就能拿到一个空字符串，即与删掉出所有字符的word1相等
        for j in range(m):
            dp[0][j] = j

        for i in range(1, n):
            for j in range(1, m):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        # print(dp)

        return dp[-1][-1]

so = Solution()

print(so.minDistance("", "a"))
print(so.minDistance("horse", "ros"))
print(so.minDistance("intention", "execution"))

print(so.minDistance_1("", "a"))
print(so.minDistance_1("horse", "ros"))
print(so.minDistance_1("intention", "execution"))