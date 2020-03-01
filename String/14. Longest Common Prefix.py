class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        prefix = strs[0] if strs else ''
        while True:
            if all(s.startswith(prefix) for s in strs):
                return prefix
            prefix = prefix[:-1]

    def longestCommonPrefix_1(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        h1 = self.longestCommonPrefix_1(strs[:len(strs)/2])
        h2 = self.longestCommonPrefix_1(strs[len(strs)/2:])
        return self.merge(h1, h2)

    def merge(self, h1, h2):
        i = 0
        while i < len(h1) and i <len(h2) and h1[i] == h2[i]:
            i+=1
        return h1[:i]

    def longestCommonPrefix_2(self, strs):
        from functools import reduce
        if not strs:
            return ""
        return reduce(self.merge, strs)


so = Solution()
print(so.longestCommonPrefix(["flower","flow","flight"]))
print(so.longestCommonPrefix(["dog","racecar","car"]))

