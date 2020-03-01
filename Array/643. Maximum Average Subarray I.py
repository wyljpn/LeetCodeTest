import itertools
import operator
class Solution(object):

    # 超时
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        gloAvg = 0
        for i in range(len(nums)-k+1):
            locAvg = sum(nums[i:i+k])/k
            gloAvg = max(locAvg, gloAvg)
        return gloAvg

    # 没超时，但还是很慢
    def findMaxAverage_1(self, nums, k):

        loc_sum = sum(nums[0:k])
        gloAvg = loc_sum*1.0/k
        for i in range(1, len(nums)-k+1):
            loc_sum = loc_sum - nums[i-1] + nums[i+k-1]
            locAvg = loc_sum*1.0/k
            gloAvg = max(locAvg, gloAvg)
        return gloAvg

    def findMaxAverage_2(self, nums, k):
        # [0]是为了头k个数的比较
        sums = [0] + list(itertools.accumulate(nums))
        return max(map(operator.sub, sums[k:], sums)) / k


so = Solution()
print(so.findMaxAverage_2([1,12,-5,-6,50,3], k=4))