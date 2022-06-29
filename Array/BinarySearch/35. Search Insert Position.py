# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4

class Solution(object):

    # 如果target在list中，则返回index。 -> 二分查找

    # 如果target没有在list中，则返回应该被插入的index。
    # 有四种情况。
    # ·target在list左边，比所有元素都小
    # ·target在list元素中
    # ·target在元素与元素之间
    # ·target在list右边，比所有元素都大

    # target <= nums[middle]

    # 左闭右闭写法
    def searchInsert_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = int(left + (right - left) / 2)
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle

        # ·target在list左边，则left=0，right=-1
        # ·target在元素与元素之间，则left>right, right+1是要插入大位置
        # ·target在list右边，比所有元素都大，则要用right+1新增一个
        # 综合考虑，插入大位置是right+1
        return right + 1

    # 左闭右开写法
    def searchInsert_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = left + (right - left) / 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle

        return right

    def searchInsert_3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i = 0
        while i < len(nums):
            # 如果nums[i]等于target，就返回当前的i
            # 如果nums[i]大于target，则i就是target要插入的index。
            if nums[i] >= target:
                return i

        return len(nums)


if __name__ == "__main__":
    so = Solution()

    print(so.searchInsert_1([1,3,5,6], 5))
    print(so.searchInsert_1([1,3,5,6], 2))
    print(so.searchInsert_1([1,3,5,6], 7))
    print(so.searchInsert_1([1,3,5,6], 0))
    print(so.searchInsert_1([], 0))