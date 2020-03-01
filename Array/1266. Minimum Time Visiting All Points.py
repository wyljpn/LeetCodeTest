class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for i in range(1, len(points)):
            try:
                if (points[i][1] - points[i-1][1]) / (points[i][0] - points[i-i][0]) == 0.5:
                    cnt += abs(points[i][0] - points[i-1][0])
                else:
                    cnt += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i - 1][1]))
            except:
                cnt += max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
        return cnt

    def minTimeToVisitAllPoints_1(self, points):
        return sum(max(abs(x-X), abs(y-Y)) for (x,y), (X, Y) in zip(points, points[1:]))


so = Solution()

print(so.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
print(so.minTimeToVisitAllPoints([[3,2],[-2,2]]))
print(so.minTimeToVisitAllPoints([[499,43],[220,-737],[640,794],[-383,759],[-244,878],[-532,214],[-189,894],[-511,63],[80,203],[-298,-311],[499,-997],[6,-140],[31,-956],[-526,347],[941,81],[-933,606]]))