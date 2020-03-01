class Solution(object):

    # 超时
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = sorted(set(arr))
        res = []
        for elem in arr:
            res.append(sorted_arr.index(elem) + 1)
        return res

    def arrayRankTransform_1(self, arr):
        # 调用 dict的get方法
        return list(map({a: i + 1 for i, a in enumerate(sorted(set(arr)))}.get, arr))


    def arrayRankTransform_2(self, A):
        import itertools
        return map(dict(zip(sorted(set(A)), itertools.count(1))).get, A)

so = Solution()

print(so.arrayRankTransform([40, 10, 20, 30]))
print(so.arrayRankTransform([100, 100, 100]))
print(so.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))

print(so.arrayRankTransform_1([40, 10, 20, 30]))
print(so.arrayRankTransform_1([100, 100, 100]))
print(so.arrayRankTransform_1([37, 12, 28, 9, 100, 56, 80, 5, 12]))
