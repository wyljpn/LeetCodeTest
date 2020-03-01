from copy import deepcopy


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # 第一行除了第一列，其余需要计算左、右、下；第一行第一列计算右、下。第一行最后一列计算左、下
        # 最后一行除了第一列，其余需要计算上、左、右；最后一行第一列计算上、右；最后一列计算上、左。
        # 中间的行，第一列计算下、右、下；最后一列计算上、左、下。

        x_len = len(M)
        y_len = len(M[0]) if x_len else 0
        res = deepcopy(M)
        for x in range(x_len):
            for y in range(y_len):
                neighbors = [
                    M[_x][_y]
                    for _x in (x-1, x, x+1)
                    for _y in (y-1, y, y+1)
                    if 0 <= _x < x_len and 0 <= _y < y_len
                ]
                res[x][y] = sum(neighbors) // len(neighbors)
        return res