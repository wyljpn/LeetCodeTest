# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
#
# Return the positive integer k. If there is no such integer, return -1.


# Example 1:
#
# Input: nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.


class Solution:
    def findMaxK(self, nums):

        # key: 负数
        # value； 正数
        dic = {}

        result = [-1]

        for i in range(len(nums)):
            if nums[i] in dic.keys():
                result.append(dic[nums[i]])
            else:
                dic[-nums[i]] = abs(nums[i])

        # print(dic)
        # print(result)

        return max(result)


if __name__ == "__main__":

    so = Solution()
    print(so.findMaxK([-1,2,-3,3]))
    print(so.findMaxK([-1,10,6,7,-7,1]))
    print(so.findMaxK([-10,8,6,7,-2,-3]))
    print(so.findMaxK([-10]))
