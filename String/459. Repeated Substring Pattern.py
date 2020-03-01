class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)//2 +1):
            if s[:i] * (len(s)//i) == s:
                return True
        return False


    # https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination
    def repeatedSubstringPattern_1(self, s):
        return s in (2*s)[1:-1]



so = Solution()

print(so.repeatedSubstringPattern("abab"))
print(so.repeatedSubstringPattern("aba"))
print(so.repeatedSubstringPattern("abcabcabcabc"))
