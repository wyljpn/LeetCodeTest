from collections import defaultdict
import collections
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """

        dic = defaultdict(int)
        for i, j in dominoes:
            dic[(min(i,j), max(i,j))] += 1

        print(dic)
        res = 0
        for val in dic.values():
            if val > 1:
                res += int(val * (val-1) / 2)
        return res

    def numEquivDominoPairs_1(self, dominoes):
        _len = len(dominoes)
        dominoes = map(tuple, map(sorted, dominoes))
        d = collections.Counter(dominoes)
        res = 0
        for k, v in d.items():
            if v >= 2:
                res += int(v * (v - 1) / 2)
        return res


so = Solution()
# print(so.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))
# print(so.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))


print(so.numEquivDominoPairs_1([[1,2],[1,2],[1,1],[1,2],[2,2]]))
# print(so.numEquivDominoPairs_1([[1,2],[2,1],[3,4],[5,6]]))
