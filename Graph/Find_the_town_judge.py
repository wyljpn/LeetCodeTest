class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # 因为label是从1到N，所以不使用下标为0的位置。
        count = [0] * (N + 1)
        for i, j in trust:
            # i不能是judge，所以如果元素值小于0，则不是judge
            count[i] -= 1
            # 被信任的次数。
            count[j] += 1
        for i in range(1, N + 1):
            # 如果次数等于N-1。则是judge
            if count[i] == N - 1:
               return i
        return -1