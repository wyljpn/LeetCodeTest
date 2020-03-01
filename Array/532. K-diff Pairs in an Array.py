import collections


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        dic = {}
        res = set()
        for num in nums:
            tmp = dic.get(num + k, float('-inf'))
            if tmp != float('-inf'):
                res.add((min(tmp, num), max(tmp, num)))

            tmp = dic.get(num - k, float('-inf'))
            if tmp != float('-inf'):
                res.add((min(tmp, num), max(tmp, num)))
            dic[num] = num

        return len(res)

    def findPairs_1(self, nums, k):
        res = 0
        # 统计每个元素出现的次数。
        # key是元素的值， value是出现的次数。
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res


so = Solution()
print(so.findPairs([1, 1, 1, 2, 1], k=1))
print(so.findPairs([3, 1, 4, 1, 5], k=2))
print(so.findPairs([1, 2, 3, 4, 5], k=1))
print(so.findPairs([1, 3, 1, 5, 4], k=0))
print(so.findPairs([6, 3, 5, 7, 2, 3, 3, 8, 2, 4], k=2))
