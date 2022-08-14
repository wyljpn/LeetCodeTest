class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # key: target - num
        # value: index of (target - num)
        record = dict()

        for index, num in enumerate(nums):
            if num not in record:
                record[target - num] = index
            else:
                return [record[num], index]