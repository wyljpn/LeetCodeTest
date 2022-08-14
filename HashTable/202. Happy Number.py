class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def calculate_happy(num):
            sum_ = 0

            while num:
                sum_ += (num % 10) ** 2
                num = num // 10

            return sum_

        record = set()

        while True:
            n = calculate_happy(n)
            if n == 1:
                return True

            if n in record:
                return False
            else:
                record.add(n)
