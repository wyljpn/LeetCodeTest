# 152. 乘积最大子数组
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
#  
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。

class Solution(object):
    def maxProduct(self, nums):

        if not nums:
            return 0
        if len(nums) ==1:
            return nums[0]
        res = nums[0]
        pre_max, pre_min = nums[0], nums[0]
        for i in range(1, len(nums)):
            left = nums[i] * pre_max
            right = nums[i] * pre_min

            pre_max = max(left, right, nums[i])
            pre_min = min(left, right, nums[i])

            res = max(res, pre_max)
        return res



so = Solution()

print(so.maxProduct([2, 3, -2, 4]))
print(so.maxProduct([-2, 0, -1]))
print(so.maxProduct([]))
print(so.maxProduct([-2, -1, 0]))
print(so.maxProduct([-2, -1, 0, 2, 3]))
print(so.maxProduct([-2, 3, -4]))
