import heapq


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums)
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    def maximumProduct_1(self, nums):
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])


so = Solution()
print(so.maximumProduct([-10, -9, -1, 0, 1, 2, 3]))
print(so.maximumProduct([1, 2, 3]))
print(so.maximumProduct([1, 2, 3, 4]))
print(so.maximumProduct([-1, -2, -3]))
