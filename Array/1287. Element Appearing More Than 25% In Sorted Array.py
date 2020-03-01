import bisect
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        threshold = n / 4
        for i in range(n):
            if arr[i] == arr[i+threshold]:
                return arr[i]


    def findSpecialInteger_1(self, arr):
        size = (len(arr)) / 4
        loose = max(1, size)
        for index in range(0, len(arr), loose):
            candidate = arr[index]
            # 返回范围内，出现过的第一个candidate的下标
            left = bisect.bisect_left(arr, candidate, max(0, index - loose), min(len(arr), index + loose))
            right = bisect.bisect_right(arr, candidate, max(0, index - loose), min(len(arr), index + loose))
            if right - left > size:
                return arr[index]

