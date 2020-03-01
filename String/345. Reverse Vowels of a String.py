class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = "AEIOUaeiou"

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)

    def reverseVowels_1(self, s):
        # 正则表达式
        import re
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

    def reverseVowels_2(self, s):
        import re
        vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)
    
so = Solution()
print(so.reverseVowels("hello"))
print(so.reverseVowels("leetcode"))
