class Solution(object):

    # 动态规划的思路：将 dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度
    # 那么题目要求的，就是这个 dp 数组中的最大者

    def lengthOfLIS(self, nums):
        size = len(nums)
        if size <= 1:
            return size
        dp = [1] * len(nums)

        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
