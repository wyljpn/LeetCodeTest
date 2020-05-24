# 4. 寻找两个正序数组的中位数
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
#
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
#  
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0

class Solution(object):

    # 自己写的，可以通过。 但是感觉不太妙
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        num = sorted(num)
        print(num)
        length = len(num)
        if length % 2 == 0:
            return (num[int(length/2)-1]+num[int(length/2)])/2
        else:
            return num[int(length/2)]


so = Solution()

print(so.findMedianSortedArrays([1, 3], [2]))
print(so.findMedianSortedArrays([1, 2], [3, 4]))
print(so.findMedianSortedArrays([1, 2, 3], [3, 4, 5]))