class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs_1(n)

    # 自己写的，35的时候超时
    def climbStairs_1(self, curStep):
        if curStep <= 1:
            return 1
        else:
            return self.one_step(curStep - 1) + self.one_step(curStep - 2)

    # Top down -TLE
    def climbStairs_2(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs_2(n - 1) + self.climbStairs_2(n - 2)

    # Bottom up, O(n) space
    def climbStairs_3(self, n):
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[n - 1]

    # Bottom up, constant space
    def climbStairs_4(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            temp = b
            b = a + b
            a = temp
        return b

    # Top down + memorization (list)
    def climbStairs_5(self, n):
        if n == 1:
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n - 1, dic)

    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n - 1, dic) + self.helper(n - 2, dic)
        return dic[n]

    # Top down + memorization(dict)
    def __init__(self):
        self.dic = {1: 1, 2: 2}

    def clibStairs_6(self, n):
        if n not in self.dic:
            self.dic[n] = self.clibStairs_6(n - 1) + self.clibStairs_6(n - 2)
        return self.dic[n]
