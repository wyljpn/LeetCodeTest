# 面试题03. 数组中重复的数字
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#
# 示例 1：
#
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3

class Solution(object):
    # 使用哈希表
    def findRepeatNumber(self, nums):
        import collections
        repeatDic = collections.defaultdict(int)
        for num in nums:
            # print(repeatDic.get(num))
            if repeatDic.get(num) is not None:
                return num
            else:
                repeatDic[num] = 1
    # 使用set
    def findRepeatNumber_2(self, nums):
        tmp_set = set()
        repeat = -1
        for i in range(len(nums)):
            tmp_set.add(nums[i])
            if len(tmp_set) < i+1:
                repeat = nums[i]
                break
        return repeat

    # 排序
    def findRepeatNumber_3(self, nums):
        nums.sort()
        # print(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]


so = Solution()

# print(so.findRepeatNumber([2,3,1,0,2,5,3]))
# print(so.findRepeatNumber([2,3,0,3]))
# print(so.findRepeatNumber([]))

print(so.findRepeatNumber_3([2,3,1,0,2,5,3]))
print(so.findRepeatNumber_3([2,3,0,3]))
print(so.findRepeatNumber_3([]))
