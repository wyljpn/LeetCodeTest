class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []

        last_s = S[0]
        num_accu = 1
        for i in range(1, len(S)):
            if last_s == S[i]:
                num_accu += 1
            elif num_accu >= 3:
                res.append([i - num_accu, i - 1])
                last_s = S[i]
                num_accu = 1
            else:
                last_s = S[i]
                num_accu = 1
        if num_accu >= 3:
            res.append([len(S) - num_accu, len(S) - 1])

        return res

    def largeGroupPositions_1(self, S):
        i, j, N = 0, 0, len(S)
        res = []
        while i < N:
            while j < N and S[j] == S[i]:
                j += 1
            if j - i >= 3:
                res.append((i, j - 1))
            i = j
        return res


so = Solution()

print(so.largeGroupPositions("abbxxxxzzy"))
print(so.largeGroupPositions("abcdddeeeeaabbbcd"))
print(so.largeGroupPositions("aaa"))
