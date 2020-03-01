class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res, carry = '', 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            curval = (i >= 0 and a[i] == '1') + (j >= 0 and b[j] == '1')
            carry, rem = divmod(curval + carry, 2)
            res = str(rem) + res
            i -= 1
            j -= 1
        return res

so = Solution()

print(so.addBinary("11", "1"))
print(so.addBinary("1010", "1011"))
