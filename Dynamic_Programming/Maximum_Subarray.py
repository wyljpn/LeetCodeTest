class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            # 取上一段的累加和与当前num中较大值
            curSum = max(num, curSum + num)
            # 取上一段累加和与curSum中较大值
            maxSum = max(maxSum, curSum)
        return maxSum

    def maxSubArray_2(self, nums):
        if not nums:
            return None
        # 保存到每个位置的最大值
        dp = [0] * len(nums)
        res = dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res


so = Solution()
print(so.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
