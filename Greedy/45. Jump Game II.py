class Solution:
    def jump(self, nums):
        
        if len(nums) == 1:
            return 0
        
        curDistance = nums[0]
        nextDistance = 0
        steps = 1
        
        for i in range(len(nums)):
            # 如果覆盖范围大于末尾item的index，退出
            if curDistance >= len(nums) -1:
                break
            
            # 更新nextDistance
            nextDistance = max(i + nums[i], nextDistance)
            
            # 如果一步到达不了，则需要多一步            
            if i >= curDistance:
                curDistance = nextDistance
                steps += 1
        
        return steps
