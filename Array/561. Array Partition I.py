class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = int(len(nums)/2)
        nums = sorted(nums)
        for i in range(n):
            res += nums[2*i]

        return res

    def arrayPairSum_1(self, nums):
        return sum(sorted(nums)[::2])



so = Solution()
print(so.arrayPairSum([1,4,3,2]))


