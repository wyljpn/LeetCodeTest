# 50. Pow(x, n)
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000

class Solution(object):
    # 方法一：快速幂 + 递归
    # 「快速幂算法」的本质是分治算法。举个例子，如果我们要计算 x^{64}，我们可以按照：
    # x -> x^2 -> x^4 -> x^8 -> x^{16} -> x^{32} -> x^{64}
    # 的顺序，从 x 开始，每次直接把上一次的结果进行平方，计算 6 次就可以得到 x^{64} 的值，而不需要对 xx 乘 6363 次 xx。

    def myPow(self, x, n):
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
