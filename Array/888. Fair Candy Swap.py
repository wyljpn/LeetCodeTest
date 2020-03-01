class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        sum_A = sum(A)
        avg = (sum_A + sum(B)) / 2
        for a in A:
            if avg - (sum_A - a) in B:
                return [a, avg - (sum_A - a)]

    def fairCandySwap_1(self, A, B):
        # sum(A) 和 sum(B) 之间相差的值是 要交换的那两个数的一半。
        dif = (sum(A) - sum(B)) / 2
        set_A = set(A)
        for b in set(B):
            if dif + b in set_A:
                return [dif + b, b]
