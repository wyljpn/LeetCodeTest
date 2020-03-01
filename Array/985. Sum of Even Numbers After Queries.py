class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_sum = 0
        res = []
        for a in A:
            if a % 2 == 0:
                even_sum += a
        for val, index in queries:
            if A[index] % 2 ==0:
                even_sum -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                even_sum += A[index]
            res.append(even_sum)
            # print(A)
        return res


so = Solution()

print(so.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))