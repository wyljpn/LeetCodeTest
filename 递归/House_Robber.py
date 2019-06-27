class Solution(object):
    # Based on the recursive formula:
    # f(0) = nums[0]
    # f(1) = max(num[0], num[1])
    # f(k) = max(f(k - 2) + nums[k], f(k - 1))
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

    def rob_2(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res[i] = max(res[i - 2] + nums[i], res[i - 1])
        return res[-1]

    def rob_3(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tmp = b
            b = max(nums[i] + a, b)
            a = tmp
        return b
