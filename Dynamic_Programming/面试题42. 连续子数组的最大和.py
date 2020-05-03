class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return
        locMax, gloMax = float("-inf"), float("-inf")
        for num in nums:
            locMax = max(num, locMax+num)
            gloMax = max(gloMax, locMax)
        return gloMax

so = Solution()

print(so.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))