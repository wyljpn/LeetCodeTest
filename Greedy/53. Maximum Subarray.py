class Solution:
    def maxSubArray(self, nums):
        
        result = float("-inf")
        count = 0
        
        for num in nums:
            # 求自序和
            count += num
            
            # 处理count > result的情况。包含count为负数的情况。
            if count > result:
                result = count
            
            # 如果自序和小于0，因为前面的自序和小于0，会拉低后面的计算。
            # 要直接置0从下一个开始算。
            if count <= 0:
                count = 0
            
        return result
