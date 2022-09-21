class Solution(object):
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[-1]


if __name__ == "__main__":
    so = Solution()

    print(so.rob([1,2,3,1]))
    print(so.rob([2,7,9,3,1]))
