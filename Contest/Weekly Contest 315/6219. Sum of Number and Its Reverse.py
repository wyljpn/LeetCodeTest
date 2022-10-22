# Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.

# Example 1:
#
# Input: num = 443
# Output: true
# Explanation: 172 + 271 = 443 so we return true.

# Example 2:
#
# Input: num = 63
# Output: false
# Explanation: 63 cannot be expressed as the sum of a non-negative integer and its reverse so we return false.
# Example 3:
#
# Input: num = 181
# Output: true
# Explanation: 140 + 041 = 181 so we return true. Note that when a number is reversed, there may be leading zeros.


class Solution:
    def sumOfNumberAndReverse(self, num):


        def reverseInt(num):

            tmp = 0

            while num > 0:
                res = num % 10

                tmp = tmp * 10 + res

                num = num // 10

            return tmp

        if num == 0:
            return True

        for i in range(num):
            if i + reverseInt(i) == num:
                # print(i)
                return True

        return False


if __name__ == "__main__":

    so = Solution()

    print(so.sumOfNumberAndReverse(443))
    print(so.sumOfNumberAndReverse(63))
    print(so.sumOfNumberAndReverse(181))
    print(so.sumOfNumberAndReverse(0))