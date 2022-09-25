class Solution:
    def findLengthOfLCIS(self, nums):
        n = len(nums)
        dp = [1 for _ in range(n)]

        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                dp[i + 1] = dp[i] + 1

        return max(dp)