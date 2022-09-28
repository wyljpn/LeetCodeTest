class Solution:
    def findLength(self, nums1, nums2):

        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]

        result = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                # 如果相等的话，就等于dp[i][j-1]+1
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                    result = max(result, dp[i][j])
            # print(dp)
        return result


    def findLength_2(self, nums1, nums2):
        dp = [0 for _ in range(len(nums2) + 1)]

        result = 0

        for i in range(1, len(nums1) + 1):
            for j in range(len(nums2), 0, -1):
                # 如果相等的话，就等于dp[i][j-1]+1
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    result = max(dp[j], result)
                else:
                    dp[j] = 0
            print(dp)
        return result