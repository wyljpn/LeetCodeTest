class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        str_tmp = ""
        for i in range(len(A)):
            str_tmp += str(A[i])
            # print("str_tmp", str_tmp)
            a = int(str_tmp, 2)
            # print(a)
            res.append(a % 5 == 0)
        return res

    def prefixesDivBy5_1(self, A):
        for i in range(1, len(A)):
            # 向右移位相当于*2。
            # 能够被5整除的话可以直接去掉。
            A[i] += A[i - 1] * 2 % 5
        return [a % 5 == 0 for a in A]


so = Solution()
print(so.prefixesDivBy5([0, 1, 1]))
print(so.prefixesDivBy5([1, 1, 1]))
print(so.prefixesDivBy5([0, 1, 1, 1, 1, 1]))
print(so.prefixesDivBy5([1, 1, 1, 0, 1]))
