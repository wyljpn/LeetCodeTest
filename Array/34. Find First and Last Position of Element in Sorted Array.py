# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.


class Solution(object):

    # 有三种情况
    # 第一种是target小于所有元素或者大于所有元素。返回[-1, -1]
    # 第二种是target在nums包含的范围内，但不与任何元素相同。返回[-1, -1]
    # 第三种是target在nums包含的范围内，并且与某些元素相同。返回相同第一个和最后一个相同元素的index
    def searchRange_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 找出右边界。
        # 如果target存在于nums中，则返回最右边的target的下标
        # 如果target不存在nums中，并且nums中存在大于target的值，则返回大于target的数中最小的值的index
        # 如果target不存在nums中，并且nums中不存在大于target的值，则返回len(nums)-1
        def getRightBorder(nums, target):

            left = 0
            right = len(nums) - 1
            # 为什么要设置成-2，而不是-1?
            # 当target大于所有元素时，rightBorder为-2
            rightBorder = -2

            while left <= right:
                middle = (left + right) // 2
                if nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
                    rightBorder = left

            return rightBorder

        def getLeftBorder(nums, target):

            left = 0
            right = len(nums) - 1
            # 当target小于所有元素时，leftBorder为-2
            leftBorder = -2

            while left <= right:
                middle = (left + right) // 2
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
                    leftBorder = right

            return leftBorder

        leftBorder = getLeftBorder(nums, target)
        rightBorder = getRightBorder(nums, target)
        # print("leftBoarder: ", leftBorder)
        # print("rightBorder: ", rightBorder)

        if leftBorder == -2 or rightBorder == -2:
            return [-1, -1]

        # 为什么不能不能是>=?
        # 因为针对第二种情况，相差是为1
        if (rightBorder - leftBorder) > 1:
            return [leftBorder + 1, rightBorder -1]

        return [-1, -1]


    # 解法2
    # 1，首先，在nums中尝试用二分查找target
    # 2，如果查找失败，target没有在nums中，则返回[-1, -1]
    # 3, 如果查找成功，target在nums中，则左右滑动指针，找到左边界和右边界
    def searchRange_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:  # 不变量：左闭右闭区间
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    return middle
            # target没有在nums中
            return -1

        index = binarySearch(nums, target)

        if index == -1:
            return [-1, -1]

        left, right = index, index

        while left >= 0 and nums[left -1] == target:
            left -= 1

        while right < len(nums) and nums[right +1] == target:
            right += 1

        return [left, right]

    # 解法3
    def searchRange_3(self, nums, target):

        def binarySearch(nums, target, lower):
            left = 0
            right = len(nums) - 1
            # 如果target大于所有nums中的元素，则ans不会被修改，会等会len(nums)
            # 如果target小于所有nums中的元素，ans会一直被修改，最终会等于0
            ans = len(nums)

            while left <= right:
                middle = left + (right - left) // 2
                # 当lower为True，判断nums[middle] >= target，用于查找左边界
                # 当lower为False，判断nums[middle] > target，用于查找右边界
                if (lower and nums[middle] >= target) or nums[middle] > target:
                    right = middle - 1
                    ans = right
                else:
                    left = middle + 1
            return ans

        rightBorder = binarySearch(nums, target, True)
        leftBorder = binarySearch(nums, target, False)

        if leftBorder <= rightBorder and rightBorder < len(nums) and nums[leftBorder] == target and nums[rightBorder] == target:
            return [leftBorder, rightBorder]
        else:
            return [-1, -1]






    # 解法4
    def searchRange_4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] >= target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1

            return left

        leftBorder = binarySearch(nums, target)  # 搜索左边界。
        rightBorder = binarySearch(nums, target + 1) - 1  # 搜索右边界
        # 情况一和情况二
        # 当target大于所有元素，则leftBorder == len(nums）
        # 当target在nums范围中，但不等于任意一个元素时，nums[leftBorder] != target
        if leftBorder == len(nums) or nums[leftBorder] != target:
            return [-1, -1]
        return [leftBorder, rightBorder]


if __name__ == "__main__":
    so = Solution()
    print(so.searchRange_1([5, 7, 7, 8, 8, 10], 8))
    print(so.searchRange_4([5, 7, 7, 8, 8, 10], 8))
    print(so.searchRange_1([5 ,7, 7, 8, 8, 10], 9))
    print(so.searchRange_4([5 ,7, 7, 8, 8, 10], 9))
    print(so.searchRange_1([5,7,7,8,8,10], 6))
    print(so.searchRange_4([5,7,7,8,8,10], 6))
    print(so.searchRange_1([], 0))
    print(so.searchRange_4([], 0))