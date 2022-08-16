class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, 0

        n = len(nums)

        while right < n:
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left