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

        # print(dp)
        return dp[-1][-1]


