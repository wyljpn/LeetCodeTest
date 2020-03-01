class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        # 选i还是i+1的判断条件：
        #   选i：
        #       第i个加第i+2元素的和 < 第i+1个元素 + 第i+3个元素
        #       1 + 3 < 2 + 4
        #       1 2 3 4 5 6 正确路径是 1 3 5 = 9
        #
        #       第i个加第i+2元素的和 < 第i+1个元素 + 第i+2个元素
        #       1 2 1 1 3 2  正确路径是1 1 1 2 = 5， 2 1 2 = 5
        #       1 1  < 2 1
        #       2 1 3 1 2 2  正确路径是1 1 2 = 4
        #       2 3 < 1 3,所以应该选择i+1


        cost_list = [0 for _ in range(len(cost))]
        cost_list[0] = cost[0]
        cost_list[1] = cost[1]

        for i in range(2, len(cost)):
            cost_list[i] = cost[i] + min(cost_list[i-1], cost_list[i-2])

        return min(cost_list[-1], cost_list[-2])


    def minCostClimbingStairs_1(self, cost):
        dp = [0]* len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        return min(dp[-2], dp[-1])

    def minCostClimbingStairs_2(self, cost):
        min_cost_0, min_cost_1 = cost[0], cost[1]

        print(min_cost_0, min_cost_1)
        for c in cost[2:]:
            min_cost_0, min_cost_1 = min_cost_1, min(min_cost_0, min_cost_1) + c

            print(min_cost_0, min_cost_1)
        return min(min_cost_0, min_cost_1)

    def minCostClimbingStairs_3(self, cost):
        pre_cost = cost[1]
        pre_pre_cost = cost[0]

        print(pre_pre_cost, pre_cost)
        for c in cost[2:]:
            pre_cost, pre_pre_cost = c + min(pre_cost, pre_pre_cost), pre_cost
            print(pre_pre_cost, pre_cost)

        return min(pre_cost, pre_pre_cost)

so = Solution()
print(so.minCostClimbingStairs_2([10,15,20]))
print(so.minCostClimbingStairs_3([10,15,20]))