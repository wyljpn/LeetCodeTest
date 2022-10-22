class Solution:
    def merge(self, intervals):
        if len(intervals) == 0: return intervals

        intervals.sort(key=lambda x: x[0])

        result = []

        result.append(intervals[0])

        for i in range(1, len(intervals)):
            last = result[-1]

            if intervals[i][0] <= last[1]:
                result[-1][1] = max(intervals[i][1], last[1])
            else:
                result.append(intervals[i])
            # print(result)

        # print(result)

        return result

if __name__ == "__main__":
    so = Solution()
    print(so.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(so.merge([[1,4],[2,3]]))