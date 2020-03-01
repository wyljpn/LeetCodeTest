class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # python 3
        new_s = ''.join(list(filter(str.isalnum, s))).lower()
        # python 2
        # new_s = ''.join(list(filter(unicode.isalnum, s))).lower()
        return new_s == new_s[::-1]

    def isPalindrome_1(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s ==s[::-1]


so = Solution()

print(so.isPalindrome("A man, a plan, a canal: Panama"))
print(so.isPalindrome("race a car"))

print(so.isPalindrome_1("A man, a plan, a canal: Panama"))
print(so.isPalindrome_1("race a car"))