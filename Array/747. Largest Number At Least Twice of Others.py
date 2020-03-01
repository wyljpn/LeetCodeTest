class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1, max_2 = 0, 0
        index_of_max_1 = 0

        for i, num in enumerate(nums):
            if num > max_1:
                max_2 = max_1
                max_1 = num
                index_of_max_1 = i
            elif num > max_2:
                max_2 = num

        return index_of_max_1 if max_1 >= 2 * max_2 else -1


    def dominantIndex_1(self, nums):
        max_num = max(nums)
        for num in nums:
            if num != max_num and max_num < num * 2:
                return -1
        return nums.index(max_num)