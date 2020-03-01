class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        s_counter = collections.Counter(s)
        for index, char in enumerate(s):
            if s_counter[char] == 1:
                return index
        return -1

    def firstUniqChar_1(self, s):
        import collections
        return min([s.find(c) for c,v in collections.Counter(s).items() if v==1] or [-1])

    # .count的运行速度更快
    def firstUniqChar_2(self, s):
        import string
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1])


so = Solution()

print(so.firstUniqChar("leetcode"))
print(so.firstUniqChar("loveleetcode"))


print(so.firstUniqChar_2("leetcode"))
print(so.firstUniqChar_2("loveleetcode"))
print(so.firstUniqChar_2("ba"))