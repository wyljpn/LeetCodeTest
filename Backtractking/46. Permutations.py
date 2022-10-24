class Solution:
    def permute(self, nums):

        result = []
        path = []

        def backtracking(nums, usageList):

            if len(nums) == len(path):
                result.append(path[:])

            for i in range(len(nums)):
                if usageList[i] == True:
                    continue
                path.append(nums[i])
                usageList[i] = True
                backtracking(nums, usageList)
                usageList[i] = False
                path.pop()

        usageList = [False] * len(nums)
        backtracking(nums, usageList)
        return result

    def permute2(self, nums):

        result = []
        path = []

        def backtracking(nums):

            if len(nums) == len(path):
                result.append(path[:])

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtracking(nums)
                path.pop()

        backtracking(nums)
        return result

