class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        grid_array = np.array(grid)
        grid_array = np.reshape(grid_array, -1)
        return len(grid_array[grid_array < 0])

    def countNegatives_1(self, grid):
        from bisect import bisect_left
        return sum(bisect_left(type('', (), {'__getitem__': lambda _, i: r[~i]})(), 0, 0, len(r)) for r in grid)


    def countNegatives_2(self, grid):
        return str(grid).count('-')

    def countNegatives_3(self, grid):
        import itertools
        return sum(a < 0 for a in itertools.chain(*grid))


so = Solution()

print(so.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(so.countNegatives([[3,2],[1,0]]))
print(so.countNegatives([[1,-1],[-1,-1]]))
print(so.countNegatives([[-1]]))