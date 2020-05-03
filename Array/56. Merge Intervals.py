class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        res = []
        intervals.sort()

        i = 0
        head, tail = intervals[0][0], intervals[0][1]
        while i < (len(intervals) -1):
            # 不连续
            if tail < intervals[i+1][0]:
                res.append([head, tail])
                head = intervals[i+1][0]
                tail = intervals[i+1][1]
            # 连续
            else:
                tail = max(tail, intervals[i+1][1])
            i += 1
        # 如果全部都连续，或者是最后与前部连续
        if not res or res[-1][-1] != tail:
            res.append([head, max(tail, intervals[-1][1])])

        return res


so = Solution()

print(so.merge([[1,3],[2,6],[8,10],[15,18]]))
print(so.merge([[1,4],[4,5]]))
print(so.merge([[1,4],[2,3]]))
print(so.merge([[1,5],[2,3],[4,9]]))
print(so.merge([[1,3],[2,6],[8,10],[15,18]]))
print(so.merge([[1,4],[0,2],[3,5]]))