class Solution:

    def robRange(self, nums):

        if len(nums) == 1:
            return nums[0]

        dp = [float("-inf") for _ in range(len(nums))]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        left = self.robRange(nums[:-1])

        right = self.robRange(nums[1:])

        return max(left, right)


