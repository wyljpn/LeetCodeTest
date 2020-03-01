class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k, end = k % len(nums), len(nums) - 1
        nums = self.reverse(nums, 0, end - k)
        nums = self.reverse(nums, end - k + 1, end)
        nums = self.reverse(nums, 0, end)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1


    def rotate_1(self,nums, k):
        k = k % len(nums)
        end = len(nums)
        for i in range(k):
            tmp = nums[-1]
            for j in range(0, end-1):
                nums[end-1-j] = nums[end-2-j]
            nums[i] = tmp
