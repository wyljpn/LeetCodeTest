class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        arr = sorted(arr)
        minimum = float('inf')
        res = []
        for n1, n2 in zip(arr[:-1:], arr[1::]):
            if n2 - n1 < minimum:
                res = [[n1, n2]]
                minimum = n2-n1
            elif n2 - n1 == minimum:
                res.append([n1, n2])

        return res

so = Solution()

print(so.minimumAbsDifference([4,2,1,3]))
print(so.minimumAbsDifference([1,3,6,10,15]))
print(so.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
