class Solution(object):

    def __init__(self):
        self.path = []
        self.paths = []

    def backtracking(self, candidates, target, sum_, startIndex):
        if sum_ > target:
            return

        if sum_ == target:
            self.paths.append(self.path[:])  # 因为是shallow copy，所以不能直接传入self.path
            return

        for i in range(startIndex, len(candidates)):
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i)
            sum_ -= candidates[i]
            self.path.pop()

    def combinationSum(self, candidates, target):

        self.backtracking(candidates, target, 0, 0)

        return self.paths



    def backtracking_2(self, candidates, target, sum_, startIndex):
        if sum_ > target:
            return

        if sum_ == target:
            self.paths.append(self.path[:])  # 因为是shallow copy，所以不能直接传入self.path
            return

        for i in range(startIndex, len(candidates)):
            if sum_ + candidates[i] > target:   # 剪枝
                return
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking_2(candidates, target, sum_, i)
            sum_ -= candidates[i]
            self.path.pop()

    def combinationSum_2(self, candidates, target):
        # 为了剪枝需要提前进行排序。因为后面的元素都比当前的大，所以如果当前元素的和大于target，则后面的元素一定大于target，无需查找。
        candidates.sort()
        self.backtracking_2(candidates, target, 0, 0)

        return self.paths