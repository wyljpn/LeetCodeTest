# Given two positive integers num1 and num2, find the integer x such that:
#
# x has the same number of set bits as num2, and
# The value x XOR num1 is minimal.
# Note that XOR is the bitwise XOR operation.
#
# Return the integer x. The test cases are generated such that x is uniquely determined.
#
# The number of set bits of an integer is the number of 1's in its binary representation.
#


# Example 1:
#
# Input: num1 = 3, num2 = 5
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0011 and 0101, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.

# Example 2:
#
# Input: num1 = 1, num2 = 12
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0001 and 1100, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.

# Constraints:
#
# 1 <= num1, num2 <= 109


# 思路
# 先求出num1和num2的二进制
# 统计num2的二进制中1和0的数量
# 根据num1的二进制，优先高位的相同，剩余的先放0，再放1。
# 把组合好的二进制转为int。

# 没有提交成功。后来写好的代码，应该是可以AC的。

class Solution:
    def minimizeXor(self, num1, num2):

        num1Binaries = bin(num1)[2:]
        num2Binaries = bin(num2)[2:]

        if len(num1Binaries) < len(num2Binaries):
            num1Binaries = "0"*(len(num2Binaries)-len(num1Binaries)) + num1Binaries

        zeros = num2Binaries.count("0")
        ones = num2Binaries.count("1")
        # print("num1Binaries: ", num1Binaries)
        # print("num2Binaries: ", num2Binaries)
        # print("zeros: ", zeros)
        # print("ones: ", ones)ta

        binaries = ""
        for s in num1Binaries:
            if s == "1" and ones > 0:
                binaries += "1"
                ones -= 1
            elif s == "1" and ones == 0:
                binaries += "0"
                zeros -= 1
            elif s == "0" and zeros > 0:
                binaries += "0"
                zeros -= 1
            elif s == "0" and zeros == 0:
                binaries += "1"
                ones -= 1

        # print("binaries: ", binaries)
        result = int(binaries, 2)
        return result



if __name__ == "__main__":
    so = Solution()
    print(so.minimizeXor(3, 5))  # 3
    print(so.minimizeXor(1, 12))  # 3
