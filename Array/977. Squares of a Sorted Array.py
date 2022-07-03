class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(len(A)):
            A[i] = pow(A[i], 2)
        min_val = min(A)
        res = [min_val]

        min_index = A.index(min_val)

        print("min", min_val, min_index)

        left = min_index - 1
        if left ==-1:
            return A
        right = min_index + 1
        if right == len(A):
            return A[::-1]

        print("ori", left, right)

        cnt = 1
        while cnt < len(A):
            print(left, right)
            if right < len(A) and left >=0 and A[left] < A[right]:
                res.append(A[left])
                left -= 1

            elif right < len(A):
                res.append(A[right])
                right += 1
            elif left >= 0:
                res.append(A[left])
                left -= 1
            cnt += 1
            # print(res)

        return res


    def sortedSquares_1(self, A):
        res = [None] * len(A)
        left, right = 0, len(A) - 1
        for index in range(len(A)-1, -1, -1):
            # 比较绝对值就行了，比计算平方快一些
            if abs(A[left]) > abs(A[right]):
                res[index] = A[left] ** 2
                left += 1
            else:
                res[index] = A[right] ** 2
                right -= 1
        return res




so = Solution()
# print(so.sortedSquares([-4,-1,0,3,10]))
# print(so.sortedSquares([-7,-3,2,3,11]))
# print(so.sortedSquares([0, 4]))
# print(so.sortedSquares([-4, 0]))
print(so.sortedSquares([-3,0,2]))
# print(so.sortedSquares([-4,-1,0,3,10]))
