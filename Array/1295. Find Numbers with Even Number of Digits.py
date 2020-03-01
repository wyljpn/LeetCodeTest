class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                cnt += 1
        return cnt

    def findNumbers_1(self, nums):

        cnt = 0
        for num in nums:
            c = 0
            while num !=0:
                num = num /10
                c += 1
            if c % 2 ==0:
                cnt += 1
        return cnt


    def findNumbers_2(self, nums):
        import math

        # log10(n) + 1 is the # of digits.
        return sum(int(math.log10(n))% 2 for n in nums)


so = Solution()

print(so.findNumbers_2( [12,345,2,6,7896]))
print(so.findNumbers_2([555,901,482,1771]))