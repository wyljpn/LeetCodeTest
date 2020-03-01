import operator
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True
        last_dif = A[1] - A[0]
        for i in range(2, len(A)):
            cur_dif = A[i]- A[i-1]
            if cur_dif * last_dif < 0:
                return False
            elif cur_dif != 0:
                last_dif = cur_dif
        return True

    def isMonotonic_1(self, A):
        print({operator.eq(i, j) for i, j in zip(A, A[1:])})
        print({operator.eq(i, j) for i, j in zip(A, A[1:])} >= {1, -1})
        # 集合的操作。 >= 是判断是否前一个集合是否包含后一个集合。
        # cmp 返回的结果是 1, 0, -1. 如果同时包含 -1, 1 则表明同时存在大于和小于的情况。
        return not {operator.eq(i, j) for i, j in zip(A, A[1:])} >= {1, -1}


so = Solution()

# print(so.isMonotonic([1,2,2,3]))
# print(so.isMonotonic([1,3,2]))
# print(so.isMonotonic([1,1,1]))
# print(so.isMonotonic([6,5,4,4]))
# print(so.isMonotonic([11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]))


print(so.isMonotonic_1([1,2,2,3]))

