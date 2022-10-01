class Solution:
    def maxSubArray(self, nums):
        # dp数组意义
        # 到下标为i为止(以nums[i]为后缀)的最大子序和
        dp = [0 for _ in range(len(nums))]

        # 初始化
        # 因为要dp[i]的计算要依赖dp[i-1]，对dp[0]进行初始化。
        dp[0] = nums[0]

        # 因为最大值不一定在最后一次计算，所以用result变量来保存最大值
        result = dp[0]

        for i in range(1, len(nums)):
            # 取累加和与当前值中最大的一个
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            result = max(dp[i], result)

        # print(dp)

        return result