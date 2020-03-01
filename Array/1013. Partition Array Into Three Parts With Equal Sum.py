import itertools


class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        quotient, remainder = divmod(sum(A), 3)
        print(quotient, remainder)
        if remainder != 0:
            return False

        acc_list = list(itertools.accumulate(A))
        # print("acc", acc_list)
        cnt = 0
        for acc in acc_list:
            if acc - (cnt * quotient) == quotient:
                cnt += 1
        # print("cnt", cnt)
        return cnt == 3

    def canThreePartsEqualSum_1(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        expected, total, count = sum(A) / 3, 0, 0

        for i in A:
            total += i
            if total == expected:
                count += 1
                total = 0

        return count == 3



    def canThreePartsEqualSum_2(self, A):
        s = sum(A)
        if s % 3 != 0:
            return False
        s /= 3
        # 只要有2个part符合，则第3个也符合
        targets = [2 * s, s]
        acc = 0
        for a in A:
            if not targets:
                return True
            acc += a
            if acc == targets[-1]:
                targets.pop()
        return False

so = Solution()

print(so.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
print(so.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
print(so.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
print(so.canThreePartsEqualSum([6, 1, 1, 13, -1, 0, -10, 20]))
