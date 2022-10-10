class Solution:
    def canJump(self, nums):
        
        if len(nums) == 1:
            return True
        
        maxRange = 0
        
        # 如果最大的范围能大于最后一个item的index，就能够到达最后一个位置
        for i in range(len(nums)):
            maxRange = max(i + nums[i], maxRange)
            
            if maxRange <= i:
                break
            
            if maxRange >= len(nums)-1:
                return True
        
        return False
