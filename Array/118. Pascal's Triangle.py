class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rows = []
        row_one = [1]
        row_two = [1, 1]

        if numRows ==0:
            return rows

        if numRows == 1:
            rows.append(row_one)
            return rows

        rows.append(row_one)
        rows.append(row_two)

        if numRows ==2:
            return rows

        for i in range(1, numRows-1):
            row = [1]
            for j in range(len(rows[i])-1):
                row.append(rows[i][j]+rows[i][j+1])
            row.append(1)
            rows.append(row)
        return rows


    def generate_1(self, numRows):
        # 生成全为1且长度符合Pascal的list
        pascal = [[1]*(i+1) for i in range(numRows)]
        # 修正为Pascal
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return  pascal

so = Solution()
# print(so.generate(5))
print(so.generate_1(5))



