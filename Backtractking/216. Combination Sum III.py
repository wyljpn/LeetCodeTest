
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        result = []
        path = []

        def backTracking(k, n, startIndex):
            if len(path) == k:
                if sum(path) == n:
                    result.append(path[:])
                return

            for i in range(startIndex, 10):
                path.append(i)
                backTracking(k, n, i + 1)
                path.pop()

        backTracking(k, n, 1)

        return result


    def combinationSum3_2(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        result = []
        path = []

        def backTracking(k, n, startIndex):
            if sum(path) > n:
                return

            if len(path) == k:
                if sum(path) == n:
                    result.append(path[:])
                return

            for i in range(startIndex, 10 - (k - len(path)) + 1):
                path.append(i)
                backTracking(k, n, i + 1)
                path.pop()

        backTracking(k, n, 1)

        return result