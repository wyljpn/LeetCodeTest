# Given two positive integers a and b, return the number of common factors of a and b.
#
# An integer x is a common factor of a and b if x divides both a and b.

# Example 1:
#
# Input: a = 12, b = 6
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
# Example 2:
#
# Input: a = 25, b = 30
# Output: 2
# Explanation: The common factors of 25 and 30 are 1, 5.


class Solution:
    def commonFactors(self, a, b):

        result = 0

        n = min(a, b)

        for i in range(1, n + 1):
            if a % i == 0 and b % i == 0:
                # print("i: ", i)
                result += 1

        return result


if __name__ == "__main__":
    so = Solution()
    print(so.commonFactors(12, 6))
    print(so.commonFactors(25, 30))