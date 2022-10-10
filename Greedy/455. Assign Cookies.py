class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
           
        # 用index来指向已经满足了的小孩子的下标，当cookie大于当前小孩子的胃口时，自增1
        index = 0

        for i in range(len(s)):
            if index < len(g) and s[i] >= g[index]: # 要加result < len(g)，否则当满足条件的饼干比小孩多的时候，index会超出len(g)
                index += 1

        return index
