class Solution:
    def wiggleMaxLength(self, nums):
        
        # 初始值设置为1，用来补最后一个匹配的值
        result = 1
        
        preDiff = 0
        
        for i in range(len(nums)-1):
            curDiff = nums[i+1] - nums[i]
            
            if curDiff * preDiff <= 0 and curDiff != 0:
                result += 1
                preDiff = curDiff
        
        return result
        
