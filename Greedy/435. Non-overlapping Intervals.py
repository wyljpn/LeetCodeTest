class Solution:
    def eraseOverlapIntervals(self, intervals):

        intervals.sort(key=lambda x: x[1])

        # print(intervals)

        result = 0

        xEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < xEnd:
                result += 1
            else:
                xEnd = intervals[i][1]

        return result


if __name__ == "__main__":
    so = Solution()
    print(so.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(so.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(so.eraseOverlapIntervals([[1,2],[2,3]]))
    print(so.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))