# 35. 搜索插入位置
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-insert-position
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def searchInsert(self, nums, target):
        # 因为是下标，所以right要是长度-1
        left, right = 0, len(nums)-1
        while left <= right:
            # mid = int((left + right) / 2)
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # 如果target大于nums中的最大元素，left就会比right大。此时的位置就是target要插入的位置。
        # 如果target小于nums中的最小元素，left就会保持0不变，知道不满足while条件。
        return left

so = Solution()

print(so.searchInsert([1,3,5,6], 5))
print(so.searchInsert([1,3,5,6], 2))
print(so.searchInsert([1,3,5,6], 7))
print(so.searchInsert([1,3,5,6], 0))
print(so.searchInsert([], 0))