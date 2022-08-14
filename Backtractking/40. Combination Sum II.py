class Solution(object):

    def __init__(self):
        self.paths = []
        self.path = []

    def backtracking(self, candidates, target, sum_, startIndex):
        if sum_ > target:
            return

        if sum_ == target:
            self.paths.append(self.path[:])
            return

        for i in range(startIndex, len(candidates)):
            # 剪枝
            if sum_ + candidates[i] > target:
                return

            # 跳过同一树层使用过的元素
            # [10,1,2,7,6,1,5], 8
            # [1, 1, 2, 5, 6, 7, 10].
            # i == startIndex为false 是为了允许一个path中使用重复出现的元素。
            # 用i > startIndex and candidates[i] == candidates[i - 1]来重复的组合。
            # 当startIndex=0，允许[1, 7] index=0； 不允许[1, 7] index =1
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue

            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i + 1)
            sum_ -= candidates[i]
            self.path.pop()


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 类似于求三数之和，求四数之和，为了避免重复组合，需要提前进行数组排序
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)

        return self.paths