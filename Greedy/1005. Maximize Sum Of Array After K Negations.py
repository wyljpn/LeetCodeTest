class Solution:
    def largestSumAfterKNegations(self, nums, k):
        
        nums = sorted(nums, key=abs, reverse=True)
        
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
        
        if k > 0:
            nums[-1] *= (-1) **k
            
        return sum(nums)
        
