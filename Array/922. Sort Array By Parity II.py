class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        n = len(A)
        i = 0
        while i < n:
            # 下标为偶数，值为奇数
            if i % 2 == 0 and A[i] % 2 == 1:
                j = i + 1
                while j < n:
                    if A[j] % 2 == 0:
                        A[i], A[j] = A[j], A[i]
                        break
                    j += 2

            # 下标为奇数，值为偶数
            if i % 2 == 1 and A[i] % 2 == 0:
                j = i + 1
                while j < n:
                    if A[j] % 2 == 1:
                        A[i], A[j] = A[j], A[i]
                        break
                    j += 2
            i += 1
        return A


    def sortArrayByParityII_1(self, A):
        # i 标记着到目前为止，最靠后的偶数的下标
        i = -1
        for j in range(len(A)):
            if i % 2 == 0 and A[i] % 2 == 0:
                i += 1
                A[i], A[j] = A[j], A[i]

        return A


so = Solution()
print(so.sortArrayByParityII([4,2,5,7]))