class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        result = 0

        for i in range(len(s)):
            if result < len(g) and s[i] >= g[result]: # 要加result < len(g)，否则当满足条件的饼干比小孩多的时候，index会超出len(g)
                result += 1

        return result
