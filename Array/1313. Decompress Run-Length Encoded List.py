class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums)-1, 2):
            res += [nums[i+1]]*nums[i]
        return res


    def decompressRLElist_1(self, nums):
        return [x for a, b in zip(nums[::2], nums[1::2]) for x in [b]*a]

so = Solution()

print(so.decompressRLElist([1,2,3,4]))