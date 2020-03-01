class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)

        quotient, carry = divmod(len(s), (2 * k))
        # print(quotient, carry)

        for i in range(quotient):
            # print(s[i*2*k:i*2*k+k], s[i*2*k:i*2*k+k][::-1])
            s[i * 2 * k:i * 2 * k + k] = s[i * 2 * k:i * 2 * k + k][::-1]
        print('list', ''.join(s))

        if carry:
            # print(s[quotient * 2 * k:quotient * 2 * k + carry])
            s[quotient * 2 * k:quotient * 2 * k + k] = s[quotient * 2 * k:quotient * 2 * k + k][::-1]

        return ''.join(s)

    def reverseStr_1(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = s[i:i + k][::-1]
        return "".join(s)


so = Solution()

print(so.reverseStr("abcdefg", 2))
print(so.reverseStr("abcdefghijkl", 2))
print(so.reverseStr("abcd", 4))
