class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)


    # 直接用公式求出前n项的和，减去nums中的所有元素的和
    def missingNumber_1(self, nums):
        n = len(nums)
        return n*(n+1)/2 - sum(nums)

    # 只能用set，list没有减法操作
    def missingNumber_2(self, nums):
        return (set(range(len(nums)+1))-set(nums)).pop()



