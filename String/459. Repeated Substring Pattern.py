class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)//2 + 1):
            if s[:i] * (len(s)//i) == s:
                return True
        return False


    # https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination
    def repeatedSubstringPattern_1(self, s):
        return s in (2*s)[1:-1]

    def repeatedSubstringPattern_2(self, s):

        if not s:
            return False

        nxt = self.getNext(s)

        if nxt[-1] != 0 and (len(s) % (len(s) - nxt[-1]) == 0):
            return True

        return False


    def getNext(self, s):
        nxt = [0] * len(s)

        j = 0

        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]

            if s[i] == s[j]:
                j += 1

            nxt[i] = j

        return nxt

so = Solution()

print(so.repeatedSubstringPattern("abab"))
print(so.repeatedSubstringPattern("aba"))
print(so.repeatedSubstringPattern("abcabcabcabc"))
