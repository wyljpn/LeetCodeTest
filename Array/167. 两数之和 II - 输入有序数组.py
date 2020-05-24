# 167. 两数之和 II - 输入有序数组
#
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
#
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:
#
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#
class Solution(object):
    # 方法 1：双指针
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            # mid = left + (right - left) // 2
            if (numbers[left] + numbers[right]) == target:
                return left + 1, right + 1
            elif (numbers[left] + numbers[right]) > target:
                right -= 1
            else:
                left += 1
        return None

    # 两次哈希表
    # step1 将数组中所有元素存入词典（哈希表），键为nums[i]，值为索引i.
    # step2 遍历数组，判断target-nums[j] 是否在词典中，且对应的索引不为其本身，即dict[target-nums[j]] 不等于j. 若满足条件，则返回.
    def twoSum_2(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        for j in range(len(nums)):
            tmp = target - nums[j]
            if (tmp in dict and dict[tmp] != j):
                return min(j+1, dict[tmp]+1), max(j+1, dict[tmp]+1)
        return None

    # 一次哈希表
    # 我们在遍历时，将target-nums[i] 存入词典，值为索引i.
    # 这样在遍历时，只要判断后续元素是否存在于词典中，即可满足条件.
    # 如：[2,7,11,15] target=9，将9-2=7 存入词典，第二个元素7在词典中存在，则返回.
    def twoSum_3(self, nums, target):
        dict={}
        for i in range(len(nums)):
            dict[nums[i]]=i
        for j in range(len(nums)):
            tmp=target-nums[j]
            if(tmp in dict and dict[tmp]!=j):
                return [j+1,dict[tmp]+1]
        return False


so = Solution()
print(so.twoSum([2, 7, 11, 15], 9))
print(so.twoSum([2, 7, 11, 15], 26))
print(so.twoSum([2, 7, 11, 15], 29))

print(so.twoSum_2([2, 7, 11, 15], 9))
print(so.twoSum_2([2, 7, 11, 15], 26))
print(so.twoSum_2([2, 7, 11, 15], 29))
