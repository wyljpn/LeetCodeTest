# 69. x 的平方根
#
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2

class Solution(object):

    # 自己写的，在leetcode提交会内存错误
    def mySqrt(self, x):
        if x <= 1:
            return x

        for  i in range(1, int(x/2)+1):
            if pow(i, 2) <= x and pow(i+1, 2)> x:
                return i


    def mySqrt_1(self, x):
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l+r)//2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

so = Solution()

print(so.mySqrt_1(4))
print(so.mySqrt_1(8))
print(so.mySqrt_1(3))
print(so.mySqrt_1(0))
print(so.mySqrt_1(1))
print(so.mySqrt_1(2147395599))