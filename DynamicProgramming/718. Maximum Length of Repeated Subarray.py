class Solution:
    def findLength(self, nums1, nums2):
        n = len(nums1) + 1
        m = len(nums2) + 1

        # dp数组的意义
        # 以下标i - 1为结尾的nums1，和以下标j - 1为结尾的nums2，最长重复子数组长度为dp[i][j]。
        # （特别注意： “以下标i-1为结尾的A” 标明一定是 以nums1[i-1]为结尾的字符串 ）
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # 初始化
        # dp[0][:]都是0
        # dp[:][0]都是0

        # 因为最大值没有固定的位置，所以要用一个变量来比较和保存最大值
        result = 0

        for i in range(1, n):
            for j in range(1, m):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(dp[i][j], result)
        # print(dp)
        for i in range(n):
            dp[i][i] = 0
            print(dp[i])
        return result

    def findLength_2(self, nums1, nums2):
        # 使用滚动数组
        n = len(nums1) + 1
        m = len(nums2) + 1

        # dp数组的意义
        # 以下标i-1为结尾的nums1，和以下标j-1为结尾的nums2，最长重复子数组长度为dp[j]。
        # （特别注意： “以下标i-1为结尾的A” 标明一定是 以nums1[i-1]为结尾的字符串 ）
        dp = [0 for _ in range(m)]

        # 初始化
        # dp[:]都是0

        # 因为最大值没有固定的位置，所以要用一个变量来比较和保存最大值
        result = 0

        for i in range(1, n):
            # 前开后闭区间
            for j in range(m-1, 0, -1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                    result = max(dp[j], result)
                # 因为使用滚动数组，当不想等的时候，要将item变成0。否则会影响后面的计算。
                else:
                    dp[j] = 0
        # print(dp)
        return result



if __name__ == "__main__":
    so = Solution()
    print(so.findLength("aaabaab","aaabaab"))
    print(so.findLength("abcabcdabc","abcabcdabc"))