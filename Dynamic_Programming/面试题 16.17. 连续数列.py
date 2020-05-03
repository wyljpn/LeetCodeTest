# 给定一个整数数组（有正数有负数），找出总和最大的连续数列，并返回总和。
#
# 示例：
#
# 输入： [-2,1,-3,4,-1,2,1,-5,4]
# 输出： 6
# 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。

class Solution(object):
    # DP
    def maxSubArray(self, nums):
        if not nums:
            return
        # localMax 计算不同片的子数组的和
        # gloMax 保存最大的子数组的和
        locMax, gloMax = float("-inf"), float("-inf")

        for i in range(len(nums)):
            locMax = max(nums[i], nums[i] + locMax)
            gloMax = max(gloMax, locMax)

        return gloMax

    def maxSubArray_1(self, nums):
        # maxSum计算nums[left]到nums[right]之间的最大连续总和
        # 最大连续总和只可能出现在数组的左右、右边，或者中间
        def maxSum(left, right):
            if left == right:
                return nums[left]
            mid = (left + right) / 2
            leftMaxSum = maxSum(left, mid)
            rightMaxSum = max(mid, right)

            sum = 0
            leftBorderMax = float("-inf")
            for i in range(mid, left - 1, -1):
                sum += nums[i]
                leftBorderMax = max(leftBorderMax, sum)

            sum = 0
            rightBorderMax = float("-inf")
            for i in range(mid + 1, right + 1, 1):
                sum += nums[i]
                rightBorderMax = max(rightBorderMax, sum)

            return max(leftMaxSum, max(rightMaxSum, leftBorderMax + rightBorderMax))

        return maxSum(0, len(nums) -1)



so = Solution()
print(so.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(so.maxSubArray([]))
print(so.maxSubArray([-1, -2]))
