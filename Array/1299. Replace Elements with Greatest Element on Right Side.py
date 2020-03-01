class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = sorted(arr)
        for i in range(len(arr)-1):
            sorted_arr.remove(arr[i])
            arr[i] = sorted_arr[-1]
        arr[-1] = -1

        return arr

    def replaceElements_1(self, arr):
        mx = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], mx = mx, max(mx, arr[i])
        return arr


so = Solution()
print(so.replaceElements([17,18,5,4,6,1]))
