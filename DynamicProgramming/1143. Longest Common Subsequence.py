class Solution:
    def longestCommonSubsequence(self, text1, text2):

        n = len(text1) + 1
        m = len(text2) + 1

        # dp数组的意义
        # 长度为[0, i-1]的字符串text1与长度为[0, j-1]的字符串text2的最长公共子序列为dp[i][j]

        # 感觉，如果第dp[i][j]依赖dp[i]中item的话，就不能使用滚动数组。
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

        print(dp)
        return dp[-1][-1]

    def longestCommonSubsequence_2(self, text1, text2):

        n = len(text1) + 1
        m = len(text2) + 1

        # dp数组的意义
        # 以下标i-1为结尾的nums1，和以下标j-1为结尾的nums2，最长重复子数组长度为dp[j]。
        # （特别注意： “以下标i-1为结尾的A” 标明一定是 以nums1[i-1]为结尾的字符串 ）
        dp = [0 for _ in range(m)]

        # 初始化
        # dp[:]都是0

        # 因为最大值没有固定的位置，所以要用一个变量来比较和保存最大值

        for j in range(1, m):
            if text2[j-1] == text1[0]:
                dp[j] = 1
                dp[j:] = [1] * (m-j)
                break

        for i in range(1, n):
            if text1[i-1] == text2[0]:
                dp[i-1] = 1
                break

        print(dp)

        for i in range(1, n):
            # print("text1[i-1]: ", text1[i-1])
            # 前开后闭区间
            for j in range(m-1, 0, -1):
                if text1[i-1] == text2[j-1]:
                    dp[j] = dp[j-1] + 1
                    # result = max(dp[j], result)
                # 因为使用滚动数组，当不想等的时候，要将item变成0。否则会影响后面的计算。
                else:
                    dp[j] = max(dp[j - 1], dp[j])
            print(dp)
        return max(dp)

if __name__ == "__main__":
    so = Solution()
    # print(so.longestCommonSubsequence("abcde","ace"))
    # print(so.longestCommonSubsequence_2("abcde","ace"))
    # print(so.longestCommonSubsequence("abcba","abcbcba"))
    # print(so.longestCommonSubsequence_2("abcba","abcbcba"))
    # print(so.longestCommonSubsequence_2("bl","yby"))
    # print(so.longestCommonSubsequence_2("abc","def"))
    # print(so.longestCommonSubsequence("bsbininm","jmjkbkjkv"))
    # print(so.longestCommonSubsequence_2("bsbininm","jmjkbkjkv"))
    # print(so.longestCommonSubsequence("pmjghexybyrgzczy","hafcdqbgncrcbihkd"))
    # print(so.longestCommonSubsequence_2("pmjghexybyrgzczy","hafcdqbgncrcbihkd")) #  gbrc
    print(so.longestCommonSubsequence("oxcpqrsvwf","shmtulqrypy"))
    print(so.longestCommonSubsequence_2("oxcpqrsvwf","shmtulqrypy")) #  gr
