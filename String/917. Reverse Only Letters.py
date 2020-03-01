class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        l, r = 0, len(S)-1
        while l < r:
            while not S[l].isalpha() and l < r:
                l += 1
            while not S[r].isalpha() and l < r:
                r -= 1

            S[l], S[r] = S[r], S[l]
            l +=1
            r -=1
        return ''.join(S)

    def reverseOnlyLetters_1(self, S):
        import re
        # 列表前面加星号作用是将列表解开成独立的参数，传入函数
        return re.sub(r'[A-Za-z]', "{}", S).format(*[c for c in S[::-1] if c.isalpha()])


so = Solution()
print(so.reverseOnlyLetters("ab-cd"))
print(so.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(so.reverseOnlyLetters("Test1ng-Leet=code-Q!"))

print(so.reverseOnlyLetters_1("ab-cd"))
print(so.reverseOnlyLetters_1("a-bC-dEf-ghIj"))
print(so.reverseOnlyLetters_1("Test1ng-Leet=code-Q!"))

