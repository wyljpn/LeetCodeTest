import itertools


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        acc_list = list(itertools.accumulate(nums))
        for i in range(len(nums)):
            if i == 0:
                if acc_list[-1] - acc_list[0] == 0:
                    return 0

            elif acc_list[-1] - acc_list[i] == acc_list[i - 1]:
                return i

        return -1


    def pivotIndex_1(self, nums):
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1


so = Solution()
print(so.pivotIndex([1, 7, 3, 6, 5, 6]))
print(so.pivotIndex([1, 2, 3]))
