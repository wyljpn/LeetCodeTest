# Input: nums = [3,7,1,6]
# Output: 5
# Explanation:
# One set of optimal operations is as follows:
# 1. Choose i = 1, and nums becomes [4,6,1,6].
# 2. Choose i = 3, and nums becomes [4,6,2,5].
# 3. Choose i = 1, and nums becomes [5,5,2,5].
# The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
# Therefore, we return 5.

class Solution:
    def minimizeArrayValue(self, nums):

        flag = True
        # print(nums)
        while flag:
            flag = False
            for i in range(len(nums) - 1, 0, -1):
                while nums[i] > nums[i - 1]:
                    nums[i] -= 1
                    nums[i - 1] += 1
                    flag = True
            # print(nums)

        # print(nums)
        return max(nums)



    def minimizeArrayValue2(self, nums):

        print(nums)
        for i in range(1, len(nums)):
            while nums[i] > nums[i - 1]:
                nums[i] -= 1
                nums[i - 1] += 1

        for i in range(len(nums) - 1, 0, -1):
            while nums[i] > nums[i - 1]:
                nums[i] -= 1
                nums[i - 1] += 1

        print(nums)

        return max(nums)


if __name__ == "__main__":

    so = Solution()
    # print(so.minimizeArrayValue([3,7,1,6]))  # 5
    # print(so.minimizeArrayValue([10, 1]))   # 10
    # print(so.minimizeArrayValue([3, 8, 5, 8]))  # 6
    # print(so.minimizeArrayValue([13,13,20,0,8,9,9]))   # 16
    # print(so.minimizeArrayValue([6,9,3,8,14]))   # 8

    # print(so.minimizeArrayValue2([3,7,1,6]))  # 5
    # print(so.minimizeArrayValue2([10, 1]))   # 10
    # print(so.minimizeArrayValue2([3, 8, 5, 8]))  # 6
    # print(so.minimizeArrayValue2([13,13,20,0,8,9,9]))   # 16
    print(so.minimizeArrayValue2([6,9,3,8,14]))   # 8
