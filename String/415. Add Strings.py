class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        res, carry = '', 0
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or carry:
            t1, t2 = 0, 0
            if i >= 0:
                t1 = int(num1[i])
            if j >= 0:
                t2 = int(num2[j])
            curval = t1 + t2
            carry, rem = divmod(curval + carry, 10)
            res = str(rem) + res
            i -= 1
            j -= 1
        return res

    def addStrings_1(self, num1, num2):
        from itertools import zip_longest
        res, c = "", 0
        for (x, y) in zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            s = (int(x) + int(y) + c)
            d, c = s % 10, int(s / 10)
            res = str(d) + res
        if c > 0:
            res = str(c) + res

        return res


so = Solution()

print(so.addStrings("0", "0"))
print(so.addStrings("123", "111"))
print(so.addStrings("13222", "2344"))
