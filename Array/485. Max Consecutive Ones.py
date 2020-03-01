class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zerocount = nums.count(0)
        if zerocount == 0:
            return len(nums)

        index = 0
        start = 0
        end = len(nums)

        ls = []

        for i in range(zerocount):
            index = nums.index(0, start, end)
            ls.append(index - start)
            start = index + 1
        ls.append(end - index)

        return max(ls)

    def findMaxConsecutiveOnes_1(self, nums):

        cnt = 0
        ans = 0
        for num in nums:
            if num != 0:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 0
        return ans

    def findMaxConsecutiveOnes_2(self, nums):

        ans = 0
        cnt = 0
        for num in nums:
           if num == 1:
            cnt += 1
           else:
              ans = max(ans,cnt)
              cnt = 0
        ans=max(ans,cnt)
        return ans


so = Solution()

print(so.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
