class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        n = len(A)
        i = 0
        while i < n:
            # 奇数
            if A[i] % 2 != 0:
                j = i + 1
                while j < n:
                    if A[j] % 2 == 0:
                        A[i], A[j] = A[j], A[i]
                        break
                    j += 1

            i += 1
        return A


    def sortArrayByParity_1(self, A):
        # i 标记着到目前为止，最靠后的偶数的下标
        i = -1
        for j in range(len(A)):
            if A[j] % 2 == 0:
                # 最靠前的奇数的下标
                i += 1
                # 更换奇数和偶数的值
                A[i], A[j] = A[j], A[i]
        return A

    def sortArrayByParity_2(self, A):
        start, end = 0, len(A)-1
        while start < end:
            m, n = A[start], A[end]
            if m % 2 == 1 and n % 2 == 0:
                A[start], A[end] = n, n
            elif m % 2 == 1:
                end -=1
            elif n % 2 ==0:
                start +=1
            else:
                start+=1
                end-=1
        return A


so = Solution()
print(so.sortArrayByParity([3, 1, 2, 4]))
print(so.sortArrayByParity([3, 2, 5, 4]))
print(so.sortArrayByParity([6, 2, 5, 1]))
