# 面试题 08.03. 魔术索引
#
# 魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，
# 若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。
#
# 示例1:
#
#  输入：nums = [0, 2, 3, 4, 5]
#  输出：0
#  说明: 0下标的元素为0
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/magic-index-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def findMagicIndex(self, nums):
        # 在[left, right]内搜索最小的魔术索引值，不存在则返回-1
        def helper(left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == mid:
                # mid是魔术索引，但是[left, right-1]也有可能存在魔术索引
                res1 = mid
                res2 = helper(left, right - 1)
                if res2 == -1:
                    return res1
                else:
                    return res2
            elif nums[mid] > mid:
                # mid不是魔术索引，但是[left, mid-1]和[num[mid]], right]中可能存在魔术索引
                # 换句话说，[mid, nums[mid] -1]之间肯定不存在魔术索引，因为是题目要求是递增数组
                res1 = helper(left, mid - 1)
                if res1 != -1:
                    return res1
                else:
                    return helper(nums[mid], right)
            elif nums[mid] < mid:
                # mid不是魔术索引，但是[left, nums[mid]]和[mid+1, right]之间可能有魔术索引
                res1 = helper(left, nums[mid])
                if res1 != -1:
                    return res1
                else:
                    return helper(mid + 1, right)

        return helper(0, len(nums) - 1)


so = Solution()

print(so.findMagicIndex([0, 2, 3, 4, 5]))
print(so.findMagicIndex([1, 1, 1]))
print(so.findMagicIndex([0, 0, 2]))
print(so.findMagicIndex([12, 13, 15]))
