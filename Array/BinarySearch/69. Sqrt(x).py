# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.


# 根据描述，要找出一个数a，使得(a*a) < target and (a+1)*(a+1) > target

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x

        while left <= right:
            middle = left + (right - left) // 2
            # 如果当前值的平方大于x，则查找当前值-1。往左查找的过程中，遇到的第一个使得平方值小于x的值，就是answer。
            if (middle * middle) > x:
                right = middle - 1
            elif (middle * middle) < x:
                left = middle + 1
            else:
                return middle

        return right

if __name__ == "__main__":
    so = Solution()
    print(so.mySqrt(4))
    print(so.mySqrt(8))
    print(so.mySqrt(9))
    print(so.mySqrt(6))
    print(so.mySqrt(10))
    print(so.mySqrt(20))
    print(so.mySqrt(0))
    print(so.mySqrt(1))
