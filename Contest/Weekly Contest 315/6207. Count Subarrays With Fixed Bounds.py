# You are given an integer array nums and two integers minK and maxK.
#
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
#
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.
#
# A subarray is a contiguous part of an array.

# Example 1:
#
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

# Example 2:
#
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

class Solution:
    def countSubarrays(self, nums, minK, maxK):

        left = 0
        right = 0
        n = len(nums)
        result = 0

        findMinK = False

        while left < n:

            # 找左边界
            while left < n and nums[left] != minK:
                left += 1
                findMinK = False

            # 找到了左边界
            if left < n and nums[left] == minK:
                right = left
                findMinK = True

            # 找右边界
            while findMinK and right < n and nums[right] != maxK:
                right += 1

            # 找到了右边界
            if right < n and nums[right] == maxK:
                result += 1
                right += 1

            while findMinK and right < n and nums[right] <= maxK:
                result += 1
                right += 1

            left += 1

        return result

if __name__ == "__main__":

    so = Solution()
    # print(so.countSubarrays([1,3,5,2,7,5], 1, 5))  # 2
    # print(so.countSubarrays([1,1,1,1], 1, 1))  # 10
    print(so.countSubarrays([35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913], 35054,945315)) # 81






