class Solution:

    def subsets(self, nums):
        path = []
        paths = []

        def backtracking(nums, startIndex):

            paths.append(path[:])

            if len(nums) == startIndex:
                return

            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()

        backtracking(nums, 0)

        return paths