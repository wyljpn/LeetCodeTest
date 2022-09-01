class Solution:
    def findTargetSumWays(self, nums, target):

        sumValue = sum(nums)

        if abs(target) > sumValue or (sumValue + target) % 2 == 1:
            return 0

        bagSize = (sumValue + target) // 2

        dp = [0 for _ in range(bagSize + 1)]

        dp[0] = 1

        for i in range(len(nums)):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        print(dp)

        return dp[bagSize]

    def findTargetSumWays_2(self, nums, target):

        sumValue = sum(nums)

        if abs(target) > sumValue or (sumValue + target) % 2 == 1:
            return 0

        bagSize = (sumValue + target) // 2

        dp = [[0 for _ in range(bagSize + 1)] for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = 1

        for i in range(len(nums)):
            for j in range(bagSize + 1):
                if (j - nums[i]) < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
            print(dp)
        # print(dp)
        return dp[-1][-1]



    def findTargetSumWays_3(self, nums, target):

        sumValue = sum(nums)

        if abs(target) > sumValue or (sumValue + target) % 2 == 1:
            return 0

        bagSize = (sumValue + target) // 2

        dp = [[0 for _ in range(bagSize + 1)] for _ in range(len(nums))]

        # 初始化
        for i in range(len(nums)):
            dp[i][0] = 1

        # 其实不初始化dp[0]也可以，因为可以使用dp[-1]
        for j in range(bagSize + 1):
            if (j - nums[0]) == 0:
                dp[0][j] += 1  # 因为元素中可能包含0，所以需要进行+=1。
        # print(dp)

        for i in range(1, len(nums)):
            for j in range(bagSize + 1):
                # 需要判断(j - nums[i]) < 0，因为nums[i]可能是负数，当nums[i]为负数时可能会报错。E.g., [999, 1], -1000. [2, 3], -5
                if (j - nums[i]) < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
        # print(dp)
        return dp[-1][-1]
