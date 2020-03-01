class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False

        flag = False
        last_val = A[0]
        for i in range(1, len(A)):
            # 上升阶段
            if A[i] > last_val and not flag:
                # 如果一直到最后都在上升，则False
                if i == len(A) - 1:
                    return False
                last_val = A[i]
            # 如果出现等于的情况
            elif A[i] == last_val:
                return False
            # 下降阶段
            elif A[i] < last_val:
                # 如果一开始就在下降，则False
                if i == 1:
                    return False
                flag = True
                last_val = A[i]
            elif flag and A[i] > last_val:
                return False

        return True

    def validMountainArray_1(self, A):

        if len(A) < 3:
            return False

        max_val = max(A)
        max_index = A.index(max_val)
        if max_index == 0 or max_index == len(A) - 1:
            return False

        last_val = A[0]
        for i in range(1, max_index):
            if A[i] <= last_val:
                return False
            last_val = A[i]
        last_val = A[max_index]
        for i in range(max_index + 1, len(A)):
            if A[i] >= last_val:
                return False
            last_val = A[i]

        return True

    def validMountainArray_2(self, A):
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j] < A[j - 1]: j -= 1
        return 0 < i == j < n - 1


so = Solution()

print(so.validMountainArray([2, 1]))
print(so.validMountainArray([3, 5, 5]))
print(so.validMountainArray([0, 3, 2, 1]))
# 峰值出现在最左的情况应该是False
print(so.validMountainArray([3, 2, 1]))
# 峰值出现在最右的情况应该是False
print(so.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
print(so.validMountainArray([1, 7, 9, 5, 4, 1, 2]))

print("---------------------")
print(so.validMountainArray_1([2, 1]))
print(so.validMountainArray_1([3, 5, 5]))
print(so.validMountainArray_1([0, 3, 2, 1]))
# 峰值出现在最左的情况应该是False
print(so.validMountainArray_1([3, 2, 1]))
# 峰值出现在最右的情况应该是False
print(so.validMountainArray_1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
print(so.validMountainArray_1([1, 7, 9, 5, 4, 1, 2]))
