# Example 1:
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#
# Example 2:
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        slow = 0
        Sum = 0
        res = float("inf")

        for fast in range(len(nums)):
            Sum += nums[fast]
            while Sum >= target:
                res = min(res, fast - slow + 1)
                Sum -= nums[slow]
                slow += 1

        return 0 if res == float("inf") else res
