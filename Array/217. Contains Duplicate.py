class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] > 1:
                return True
        return False


    def containsDuplicate_1(self, nums):
        return True if len(set(nums)) < len(nums) else False