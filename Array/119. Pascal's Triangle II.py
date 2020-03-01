class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        row_zero = [1]
        row_one = [1, 1]
        row_two = [1, 2, 1]

        if rowIndex == 0:
            return row_zero

        if rowIndex == 1:
            return row_one

        if rowIndex == 2:
            return row_two

        last_row = row_two
        i_row = []
        for i in range(2, rowIndex):
            i_row = [1] * (i + 2)
            for j in range(1, len(last_row)):
                i_row[j] = last_row[j - 1] + last_row[j]
            last_row = i_row

        return i_row

    def getRow_1(self, rowIndex):
        row = [1] * (rowIndex + 1)
        # 计算第2行道第rowIndex行的Pascal.
        # i代表第i行的Pascal, 第i行的Pascal占前(rowIndex+1)个元素。
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                row[i - j] += row[i - j - 1]
        return row


so = Solution()
# print(so.getRow(2))
# print(so.getRow(3))
print(so.getRow(4))
print(so.getRow(5))
