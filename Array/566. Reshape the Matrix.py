import numpy as np
import itertools
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        nums_np = np.array(nums)
        if r * c != np.size(nums_np):
            return nums

        nums_np = nums_np.reshape([r,c])

        return nums_np.tolist()

    def matrixReshape_1(self, nums, r, c):

        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums


    def matrixReshape_2(self, nums, r, c):
        # see https://stackoverflow.com/questions/33541947/what-does-the-built-in-function-sum-do-with-sumlist
        flat = sum(nums, [])
        if len(flat) != r * c:
            return nums
        # 看不懂。
        # see http://stupidpythonideas.blogspot.com/2013/08/how-grouper-works.html
        tuples = zip(*([iter(flat)] * c))

        return map(list, tuples)

    def matrixReshape_3(self, nums, r, c):

        if r * c != len(nums) * len(nums[0]):
            return nums
        # itertools.chain(*iterables) 可将多个序列处理为单个序列。
        # list前面加*是将二维list进行拆分，结果是多个一维list
        it = itertools.chain(*nums)
        # itertools.islice(iterable, stop)
        # itertools.islice(iterable, start, stop[, step])
        return [list(itertools.islice(it, c)) for _ in range(r)]



so = Solution()
print(so.matrixReshape_2([[1,2],[3,4]],1,4))
# print(so.matrixReshape(nums = [[1,2], [3,4]],r = 2, c = 4))