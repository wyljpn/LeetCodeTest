from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        threshold = len(nums)/2
        res = []
        for num in nums:
            dic[num] += 1
        for key, value in dic.items():
            if value >= threshold:
                res.append(key)
        return res

    def majorityElement_1(self, nums):

        return sorted(nums)[len(nums) // 2]


    # two pass + dictionary
    def majorityElement_2(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in nums:
            if dic[num] > len(nums)//2:
                return num

