class Solution:
    def permuteUnique(self, nums):

        result = []
        path = []

        def backtracking(nums, usageList):
            if len(nums) == len(path):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and usageList[i-1] == False:
                    continue

                if usageList[i] == False:
                    usageList[i] = True
                    path.append(nums[i])
                    backtracking(nums, usageList)
                    path.pop()
                    usageList[i] = False

        usageList = [False] * len(nums)

        backtracking(sorted(nums), usageList)

        return result

