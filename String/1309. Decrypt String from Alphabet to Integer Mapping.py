class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = dict(zip(["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["a", "b", "c", "d", "e", "f", "g", "h", "i"]))

        for i in range(10, 27):
            dic[str(i) + '#'] = chr(96 + i)

        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                res.append(dic[s[i - 2:i + 1]])
                i -= 3
            else:
                res.append(dic[s[i]])
                i -= 1
        return ''.join(res)[::-1]

    def freqAlphabets_1(self, s):
        import re
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))


so = Solution()

print(so.freqAlphabets("10#11#12"))
print(so.freqAlphabets("1326#"))
print(so.freqAlphabets("25#"))
