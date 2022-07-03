# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        left = 0
        right = num


        while left <= right:
            middle = left + (right - left) // 2

            if (middle * middle) > num:
                right = middle - 1
            elif (middle * middle) < num:
                left = middle + 1
            else:
                return True
        return False


if __name__ =="__main__":
    so = Solution()

    print(so.isPerfectSquare(4))
    print(so.isPerfectSquare(3))
    print(so.isPerfectSquare(6))
    print(so.isPerfectSquare(9))
