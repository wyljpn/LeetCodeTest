class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(s[:i].count('L') * 2 == i for i in range(len(s)))

    def balancedStringSplit_1(self, s):
        res = cnt = 0
        for c in s:
            cnt += 1 if c == 'L' else -1
            if cnt ==0:
                res+=1
        return res

so = Solution()
print(so.balancedStringSplit("RLRRLLRLRL"))
print(so.balancedStringSplit("RLLLLRRRLR"))
# print(so.balancedStringSplit("LLLLRRRR"))
# print(so.balancedStringSplit("RLRRRLLRLL"))
