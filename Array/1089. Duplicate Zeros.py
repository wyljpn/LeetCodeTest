class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

        i = 0
        while i < len(arr) - 1:
            # print(i)
            if arr[i] == 0:
                arr[i + 2:] = arr[i + 1:-1]
                arr[i + 1] = 0
                i += 2
            else:
                i += 1
        print(arr)

    # mp记录每个下标对应着原先arr的下标
    def duplicateZeros_1(self, arr):
        n = len(arr)
        zeros = 0
        i = 0
        mp = dict()
        while i + zeros < n:
            mp[i + zeros] = i
            if arr[i] == 0:
                zeros += 1
                mp[+zeros] = i
        for i in range(n - 1, -1, -1):
            arr[i] = arr[mp[i]]

    #  improved version of solution 2
    def duplicateZeros_2(self, arr):
        n = len(arr)
        zeros = 0
        i = 0
        while i + zeros < n:
            zeros += arr[i] == 0
            i += 1
        # i+zeros is at most n+1
        i -= 1
        while zeros > 0:
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                arr[i + zeros] = arr[i]
            i -= 1


so = Solution()

print(so.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(so.duplicateZeros([1, 2, 3]))
print(so.duplicateZeros([0, 0, 0]))
print(so.duplicateZeros([0, 0, 1]))
print(so.duplicateZeros([1, 0, 0]))
