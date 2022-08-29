
class Solution(object):
    def wei_bag_problem(self, bag_size, weight, value):
        rows, cols = len(weight), bag_size + 1
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        # 初始化dp数组.
        for i in range(rows):
            dp[i][0] = 0

        first_item_weight, first_item_value = weight[0], value[0]
        for j in range(cols):
            if j >= first_item_weight:
                dp[0][j] = first_item_value

        # 更新dp数组: 先遍历物品, 再遍历背包.
        for i in range(1, rows):
            cur_weight, cur_val = weight[i], value[i]
            for j in range(1, cols):
                if j < cur_weight:
                    dp[i][j] = dp[i - 1][j]  # 所以不装当前物品.
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight] + cur_val)

        return dp[-1][-1]

    # 滚动数组
    def wei_bag_problem_2(self, bag_size, weight, value):
        dp = [0] * (len(weight) + 1)

        for i in range(len(weight)):
            for j in range(bag_size, weight[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

        return dp[-1]
