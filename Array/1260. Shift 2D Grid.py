class Solution(object):

    # Method 1: space O(m * n)
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        m, n = len(grid), len(grid[0])
        # In case k >= m * n, use k % (m * n) to avoid those whole cycles of m * n operations.
        start = m * n - k % (m * n)
        ans = []

        # 从将要变成res的第一个元素开始
        for i in range(start, m * n + start):
            # 应对 m*n 到 m*n + start的部分
            j = i % (m * n)
            # 要被移动的元素的行数和列数
            r, c = j // n, j % n
            # 如果是新的一行
            if not (j - start) % n:
                ans.append([])
            ans[-1].append(grid[r][c])

        return ans

    # Method 2: space O(1) - excluding return list
    # 1.Imagine the grid to be a 1-D array of size m * n;
    # 2.reverse the whole array;
    # 3.reverse the first k elements
    # 4.reverse the remaing m * n - k element.
    def shiftGrid_1(self, grid, k):

        def reverse(lo, hi):
            while lo<hi:
                r, c, i, j = lo // cols, lo % cols, hi // cols, hi % cols
                grid[r][c], grid[i][j] = grid[i][j], grid[r][c]
                lo += 1
                hi -= 1

        rows, cols = len(grid), len(grid[0])
        k %= rows * cols
        reverse(0, rows * cols - 1)
        reverse(0, k - 1)
        reverse(k, rows * cols - 1)
        return grid
