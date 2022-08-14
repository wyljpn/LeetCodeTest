class Solution(object):

    def __init__(self):
        self.path = []
        self.paths = []

    def backTracking(self, candidates, target, sum_, startIndex):
        if sum_ > target:
            return

        if sum_ == target:
            self.paths.append(self.path[:])  # 因为是shallow copy，所以不能直接传入self.path
            return

        for i in range(startIndex, len(candidates)):
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backTracking(candidates, target, sum_, i)
            sum_ -= candidates[i]
            self.path.pop()

    def combinationSum(self, candidates, target):

        self.backtracking(candidates, target, 0, 0)

        return self.paths
