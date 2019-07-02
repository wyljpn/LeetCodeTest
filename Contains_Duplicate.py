class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                return True
        return False

    def containsDuplicate_2(self, nums):
        return len(nums) != len(set(nums))

    def containsDuplicate_3(self, nums):
        return True if len(set(nums)) < len(nums) else False


so = Solution()
print(so.containsDuplicate([1, 2, 3, 1]))
print(so.containsDuplicate_2([1, 2, 3, 1]))
