class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_same = [True if a ==b else False for a, b in zip(nums, sorted(nums))]
        # 总的数量 - 头不需要重新排序的数量 - 尾不需要重新排序的数量
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)

    def findUnsortedSubarray_1(self, nums):
        res = [i for (i, (a, b)) in enumerate(zip(nums, sorted(nums))) if a != b]
        return 0 if not res else res[-1] - res[0] + 1


so = Solution()

# print(so.findUnsortedSubarray([2,1]))
print(so.findUnsortedSubarray([1,3,2,2,2]))