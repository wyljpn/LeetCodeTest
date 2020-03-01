class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 从后往前判断。
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        # nums2中有小于nums1中的最小值的情况
        if n > 0:
            nums1[:n] = nums2[:n]

    def merge_1(self, nums1, m, nums2, n):
        nums1[m:m + n] = nums2[:n]
        nums1.sort()


so = Solution()
print(so.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
