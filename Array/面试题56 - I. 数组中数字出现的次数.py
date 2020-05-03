# 面试题56 - I. 数组中数字出现的次数
#
# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
#
#  
#
# 示例 1：
#
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]


class Solution(object):
    def singleNumbers(self, nums):
        import functools
        # 全体取异或
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1

        # 找出不为 0 的最低位
        while div & ret == 0:
            div <<= 1

        a, b = 0, 0

        for n in nums:
            # true的话，分到第一组
            if n & div:
                # 这一组里进行异或
                a ^= n
            # false的话，分到第二组
            else:
                b ^= n
        return [a, b]
