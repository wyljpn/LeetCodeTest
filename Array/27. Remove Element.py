# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        fast = slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow

    def removeElement_2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            # 查找等于val的index
            while left <= right and nums[left] != val:
                left += 1

            # 查找不等于val的index
            while left <= right and nums[right] == val:
                right -= 1

            # print("left :", left)
            # print("right :", right)

            # 交换
            # 如果left和right中间没有val的话，就退出
            if left <= right:
                nums[left] = nums[right]
                left += 1
                right -= 1

        return left


if __name__ == "__main__":
    so = Solution()
    print(so.removeElement([3, 2, 2, 3], 3))
    print(so.removeElement_2([3, 2, 2, 3], 3))
    print(so.removeElement([3, 2, 2, 3], 5))
    print(so.removeElement_2([3, 2, 2, 3], 5))
    # print(so.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    # print(so.removeElement_2([0, 1, 2, 2, 3, 0, 4, 2], 2))