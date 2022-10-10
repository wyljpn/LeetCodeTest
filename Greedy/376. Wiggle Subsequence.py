class Solution:
    # 贪心
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
        
    # 动态规划
    def wiggleMaxLength2(self, nums):
        
        # dp数组的意义
        # 每个item是一个长度为2的数组，
        #   第一个值代表把当前节点当成波峰时的Wiggle Subsequence最大长度
        #   第一个值代表把当前节点当成波谷时的Wiggle Subsequence最大长度
        dp = []
        
        for i in range(len(nums)):
            
            # 给当前值设置一个初始值，可以用来处理当前值与之前的值相同的情况
            dp.append([1, 1])
            
            for j in range(i):
                # 当前值被当作波峰时
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                # 当前值被当作波谷时
                elif nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                    
        # print(dp)
        return max(dp[-1])
