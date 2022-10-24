class Solution:
    def findSubsequences(self, nums):

        result = []
        path = []

        def backtracking(nums, startIndex):
            if len(path) >= 2:
                result.append(path[:])

            # Base Case（可忽略）
            if startIndex == len(nums):
                return

            # 单层递归逻辑
            # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
            usage_list = set()
            # 同层横向遍历
            for i in range(startIndex, len(nums)):
                # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
                if (path and nums[i] < path[-1]) or nums[i] in usage_list:
                    continue
                usage_list.add(nums[i])
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()


        backtracking(nums, 0)

        return result


    def findSubsequences2(self, nums):

        result = []
        path = []

        def backtracking(nums, startIndex):
            if len(path) >= 2:
                result.append(path[:])

            # Base Case（可忽略）
            if startIndex == len(nums):
                return

            # 单层递归逻辑
            # 同层横向遍历
            for i in range(startIndex, len(nums)):
                # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
                if (path and nums[i] < path[-1]) or nums[i] in nums[startIndex:i]:
                    continue
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()


        backtracking(nums, 0)

        return result


    def findSubsequences3(self, nums):

        result = []
        path = []

        def backtracking(nums, startIndex):
            if len(path) >= 2:
                result.append(path[:])

            # Base Case（可忽略）
            if startIndex == len(nums):
                return

            # 单层递归逻辑
            # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
            usage_list = [False] * 201  # 使用列表去重，题中取值范围[-100, 100]
            # 同层横向遍历
            for i in range(startIndex, len(nums)):
                # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
                if (path and nums[i] < path[-1]) or usage_list[nums[i]+100] == True:
                    continue
                usage_list[nums[i] + 100] = True
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)

        return result

if __name__ == "__main__":
    so = Solution()

    print(so.findSubsequences([4,6,7,7]))
    print(so.findSubsequences2([4,6,7,7]))