class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return
        return set(range(1, len(nums) + 1)) - set(nums)

    # 把出现过的num对应的下标赋值为负数。
    # 最后为正数的num对应的下标就是没出现过的数。
    def findDisappearedNumbers_1(self, nums):

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
