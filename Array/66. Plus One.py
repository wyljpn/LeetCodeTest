class Solution(object):

    # 把list先转成str，再转成int。加一之后再转回list。
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strDigits = str(digits)[1:-1]

        intDigitsPlusOne = int(strDigits.replace(', ', "")) + 1

        strDigitsPlusOne = list(str(intDigitsPlusOne))

        return strDigitsPlusOne

    # 按位求出数字的大小，加一之后转成str，再转回list
    def plusOne_1(self, digits):

        intDigits = 0
        for i in range(1, len(digits) + 1):
            intDigits += pow(10, i - 1) * digits[-i]
        intDigits += 1

        return list(str(intDigits))

    # 从个位开始，每位都加进位carry。如果最高位有进位，则往list中insert进位。
    def plusOne_2(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            # divmod返回(商, 余数)。
            carry, digits[i] = divmod(digits[i] + carry, 10)
        if carry:
            digits.insert(0, carry)
        return digits

    def plusOne_3(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i] + carry
            if num > 9:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] = num
        # 使用这个判断条件的话，运行速度比较快。
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


so = Solution()
# print(so.plusOne([1,2,3]))
# print(so.plusOne_1([1,2,3]))
# print(so.plusOne_2([1, 2, 3]))
print(so.plusOne_3([1, 2, 3]))
