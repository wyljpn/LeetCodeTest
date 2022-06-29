class Solution(object):

    # 左闭右闭区间的写法
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        # 因为规定了使用左闭右闭区间，所以left可以允许等于right。例如[1, 1]。
        # 查找范围包含右边界
        while left <= right:
            middle = (left + right) / 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle

        return -1


    # 左闭右开区间的写法
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        # 查找范围不包含右边界，所以使用len(nums)
        right = len(nums)
        # 因为规定了使用左闭右开区间，所以left不可以允许等于right。例如[1, 1)
        # 查找范围不包含右边界
        while left < right:
            middle = (left + right) / 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                # 查找范围不包含右边界，所以使用middle-1
                right = middle
            else:
                return middle

        return -1