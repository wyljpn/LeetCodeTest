# Example 1:
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Example 2:
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution(object):

    # 快慢指针
    # 当fast指向的元素与slow指向的元素不同的时候，就增加slow，并且nums[slow] = nums[fast]
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1


if __name__ =="__main__":
    so = Solution()

    print(so.removeDuplicates([1, 1, 2]))
    print(so.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(so.removeDuplicates([0, 0, 0, 0]))
    print(so.removeDuplicates([0, 2, 2, 4]))