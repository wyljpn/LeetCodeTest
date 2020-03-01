class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        index = -1
        try:
            index = haystack.index(needle)
        except:
            index = -1
        return index

    def strStr_1(self, haystack, needle):
        return haystack.find(needle)

    def strStr_2(self, haystack, needle):
        for i in range(len(haystack) - len(needle) - 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


    def strStr_3(self, haystack, needle):
        def kmp(str_):
            b, prefix = 0, [0]
            for i in range(1, len(str_)):
                while b > 0 and str_[i] != str_[b]:
                    b = prefix[b - 1]
                if str_[b] == str_[i]:
                    b += 1
                else:
                    b = 0
                prefix.append(b)
            return prefix

        str_ = kmp(needle + '#' + haystack)
        n = len(needle)
        if n == 0:
            return n
        for i in range(n + 1, len(str_)):
            if str_[i] == n:
                return i - 2 * n
        return -1

so = Solution()

print(so.strStr("hello", "ll"))
print(so.strStr("aaaaa", "bba"))
print(so.strStr("mississippi", "issip"))

print(so.strStr_3("hello", "ll"))
print(so.strStr_3("aaaaa", "bba"))
print(so.strStr_3("mississippi", "issip"))
print(so.strStr_3("mississippi", ""))
