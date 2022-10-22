class Solution:
    def partition(self, s):


        result = []
        path = []

        def backtracking(s, start_index: int):
            # Base Case
            if start_index >= len(s):
                result.append(path[:])
                return

            # 单层递归逻辑
            for i in range(start_index, len(s)):
                # 此次比其他组合题目多了一步判断：
                # 判断被截取的这一段子串([start_index, i])是否为回文串
                temp = s[start_index:i + 1]
                if temp == temp[::-1]:  # 若反序和正序相同，意味着这是回文串
                    path.append(temp)
                    backtracking(s, i + 1)  # 递归纵向遍历：从下一处进行切割，判断其余是否仍为回文串
                    path.pop()
                else:
                    continue
        '''
        递归用于纵向遍历
        for循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到一种方法
        类似组合问题，为了不重复切割同一位置，需要start_index来做标记下一轮递归的起始位置(切割线)
        '''
        backtracking(s, 0)
        return result
