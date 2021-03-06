# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4

class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            # 左边是有序数组
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 右边是有序数组
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


so = Solution()

print(so.search([4, 5, 6, 7, 0, 1, 2], 0))
print(so.search([4, 5, 6, 7, 0, 1, 2], 3))
print(so.search([4, 5, 0, 1, 2], 0))
print(so.search([], 0))
print(so.search([2], 0))
print(so.search([2], 2))
print(so.search([1, 3], 1))
print(so.search([3, 1], 3))
print(so.search([3, 1], 1))
