import collections
from functools import reduce
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        cnt_dic = {}
        for i in range(len(A)):
            # print(collections.Counter(A[i]))
            cnt_dic[i] = (collections.Counter(A[i]))


        res = []
        for key, val in cnt_dic[0].items():
            for i in range(1,len(A)):
                val = min(val, cnt_dic[i].get(key, 0))
            for i in range(val):
                res.append(key)
        return res

    def commonChars_1(self, A):
        res = collections.Counter(A[0])
        print(res)
        print(res.elements())
        for a in A:
            # 并的操作，保留同时出现的元素
            res &= collections.Counter(a)
        return list(res.elements())


    def commonChars_2(self, A):
        return list(reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())



so = Solution()

# print(so.commonChars(["bella","label","roller"]))
# print(so.commonChars(["cool","lock","cook"]))

print(so.commonChars_1(["bella","label","roller"]))
# print(so.commonChars_1(["cool","lock","cook"]))

