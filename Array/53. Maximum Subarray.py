class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cumSum = maxSum = nums[0]
        for num in nums[1:]:
            # 取上一段的累加和与当前num中较大值
            cumSum = max(num, num + cumSum)
            # 取上一段累加和与curSum中较大值
            maxSum = max(cumSum, maxSum)
        return maxSum


so = Solution()
print(so.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
