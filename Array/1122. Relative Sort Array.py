import collections
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        last = len(arr2)
        k = {b: i for i, b in enumerate(arr2)}
        return sorted(arr1, key=lambda elem: k.get(elem, last + elem))

so = Solution()
print(so.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))