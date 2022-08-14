class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """

        from collections import defaultdict
        rec, cnt = defaultdict(lambda: 0), 0

        for n1 in nums1:
            for n2 in nums2:
                rec[n1 + n2] += 1

        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                cnt += rec.get(key, 0)

        return cnt