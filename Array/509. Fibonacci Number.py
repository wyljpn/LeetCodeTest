class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        pre_pre = 0
        pre = 1
        if N == 0:
            return 0
        if N == 1:
            return 1

        for i in range(2, N + 1):
            pre, pre_pre = pre + pre_pre, pre

        return pre

    # naive recursive
    def fib_1(self, N):
        if N == 0: return 0
        if N == 1: return 1
        return self.fib_1(N - 1) + self.fib_1(N - 2)

    # memorized recursive
    memo = {}

    def fib_2(self, N):
        if N == 0: return 0
        if N == 1: return 1
        if N - 1 not in self.memo: self.memo[N - 1] = self.fib_2(N - 1)
        if N - 2 not in self.memo: self.memo[N - 2] = self.fib_2(N - 2)
        return self.memo[N - 1] + self.memo[N - 2]

    # iterative space-optimized
    def fib_3(self, N):
        if N == 0: return 0
        memo = [0, 1]
        for _ in range(2, N + 1):
            memo = [memo[-1], memo[-1] + memo[-2]]

        return memo[-1]

    # can use a tuple for better performance
    def fib_4(self, N):
        if N == 0: return 0
        memo = (0, 1)
        for _ in range(2, N + 1):
            memo = (memo[-1], memo[-1] + memo[-2])

        return memo[-1]


so = Solution()
print(so.fib(0))
print(so.fib(1))
print(so.fib(2))
print(so.fib(3))
print(so.fib(4))
print(so.fib(5))
print(so.fib(6))
print(so.fib(7))
