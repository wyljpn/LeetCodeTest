# 1095. 山脉数组中查找目标值
#
# 给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。
#
# 如果不存在这样的下标 index，就请返回 -1。
#
#  
#
# 何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：
#
# 首先，A.length >= 3
#
# 其次，在 0 < i < A.length - 1 条件下，存在 i 使得：
#
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
#  
#
# 你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：
#
# MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
# MountainArray.length() - 会返回该数组的长度
#
#
# 示例 1：
#
# 输入：array = [1,2,3,4,5,3,1], target = 3
# 输出：2
# 解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray(object):
    def get(self, index):
        """
        :type index: int
        :rtype int
        """

    def length(self):
        """
        :rtype int
        """


def binary_search(moutain, target, l, r, key=lambda x: x):
    target = key(target)
    while l <= r:
        mid = (l + r) // 2
        cur = key(moutain.get(mid))
        if cur == target:
            return mid
        elif cur < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


class Solution(object):
    def findInMountainArray(self, target, mountain_arr):

        l, r = 0, mountain_arr.length() - 1

        # find peak
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l

        index = binary_search(mountain_arr, target, 0, peak)

        if index != -1:
            return index
        index = binary_search(mountain_arr, target, peak + 1, mountain_arr.length() - 1, lambda x: -x)
        return index

so = Solution()
