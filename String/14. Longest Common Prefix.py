class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        prefix = strs[0] if strs else ''
        # Trim strs[0] until the trimed string is the common prefix
        while True:
            if all(s.startswith(prefix) for s in strs):
                return prefix
            prefix = prefix[:-1]

    def longestCommonPrefix_2(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        h1 = self.longestCommonPrefix_2(strs[:len(strs)/2])
        h2 = self.longestCommonPrefix_2(strs[len(strs)/2:])
        return self.merge(h1, h2)

    def merge(self, h1, h2):
        i = 0
        while i < len(h1) and i < len(h2) and h1[i] == h2[i]:
            i += 1
        return h1[:i]

    def longestCommonPrefix_3(self, strs):
        from functools import reduce
        if not strs:
            return ""
        return reduce(self.merge, strs)

    def longestCommonPrefix_4(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        # i is index of a character in a string
        for i in range(len(strs[0])):
            # j is the index of a string in the list
            for j in range(1, len(strs)):
                try:
                    if strs[0][i] == strs[j][i]:
                        continue
                    else:
                        # strs[0][:i+1] is not common prefix
                        return strs[0][:i]
                # When len(strs[0]) > later strings, return strs[0]
                except:
                    return strs[j]
        # strs[0] is the common prefix
        return strs[0]

so = Solution()
print(so.longestCommonPrefix(["flower","flow","flight"]))
print(so.longestCommonPrefix(["dog","racecar","car"]))

