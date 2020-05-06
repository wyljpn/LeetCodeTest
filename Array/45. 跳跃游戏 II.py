# 45. 跳跃游戏 II
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 示例:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
class Solution(object):
    # 求出到每个位置的最小跳跃数。会超时
    def jump(self, nums):
        arr = [0] * len(nums)
        n, rightmost = len(nums), 0
        for i in range(n):
            for step in range(1, nums[i] + 1):
                if (i + step) >= n:
                    break
                if arr[i + step] == 0:
                    arr[i + step] = arr[i] + 1
        return arr[-1]

    # 贪心法。
    # 如果我们「贪心」地进行正向查找，每次找到可到达的最远位置，就可以在线性时间内得到最少的跳跃次数。
    def jump_2(self, nums):
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                # 在当前位置，最远能跳的距离
                maxPos = max(maxPos, i + nums[i])
                # 在这一轮的候选项中，选择能跳的最远的下标
                if i == end:
                    end = maxPos
                    step += 1
        return step



so = Solution()

print(so.jump([2, 3, 1, 1, 4]))
print(so.jump([2]))
print(so.jump([2, 0, 1]))
