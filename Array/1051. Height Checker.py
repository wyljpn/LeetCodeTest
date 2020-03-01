class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if h[i] != heights[i]:
                cnt +=1
        return cnt


    def heightChecker_1(self, heights):
        return sum (h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

