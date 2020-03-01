class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}

        for index, num in enumerate(nums):
            dic[num] = dic.get(num, index)
            if dic[num]!=index and index-dic[num]<=k:
                return True
            else:
                dic[num] = index

        return False

    def containsNearbyDuplicate_1(self, nums, k):

        dic = {}
        for index, num in enumerate(nums):
            if num in dic and index - dic[num] <= k:
                return True
            dic[num] = index
        return False
