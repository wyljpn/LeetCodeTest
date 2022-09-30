class Solution:
    def maxUncrossedLines(self, nums1, nums2):

        n = len(nums1) + 1
        m = len(nums2) + 1

        # dp数组的意义
        # 在下标为i-1的nums1和j-1的nums2中，出现最大长度的公共子序列的长度
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # 初始化
        # nums1[0]和nums2[0]相等时，dp[1][1]=0+1=1
        # 初始值为0

        for i in range(1, n):
            for j in range(1, m):
                # 相等时，直接+1
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 不想等的时候，等于左边或者上边的最大值
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # print(dp)
        return dp[-1][-1]





