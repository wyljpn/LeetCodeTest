class Solution:
    def subsetsWithDup(self, nums):

        paths = []
        path = []
        nums.sort()  # 去重需要先对数组进行排序

        def backtracking(nums, startIndex):
            paths.append(path[:])

            # 终止条件
            if len(nums) == startIndex:
                return

            for i in range(startIndex, len(nums)):
                # 数层去重
                if i > startIndex and nums[i] == nums[i - 1]:  # 去重
                    continue
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()

        backtracking(nums, 0)

        return paths
