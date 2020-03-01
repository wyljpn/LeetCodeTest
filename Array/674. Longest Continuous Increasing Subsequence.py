class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        loc_longest = glo_longest = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                loc_longest += 1
                glo_longest = max(loc_longest, glo_longest)
            else:
                loc_longest = 1
        return glo_longest