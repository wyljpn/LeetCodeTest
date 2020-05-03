# 1248. 统计「优美子数组」
#
# 给你一个整数数组 nums 和一个整数 k。
#
# 如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
#
# 请返回这个数组中「优美子数组」的数目。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        # 下标对应奇数的个数，值对应前i项中奇数个数相同的的数量。
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        odd, ans = 0, 0
        for num in nums:
            if num % 2 == 1:
                odd += 1
            if odd >= k:
                ans += cnt[odd - k]
            cnt[odd] += 1
        return ans



so = Solution()

print(so.numberOfSubarrays([1, 1, 2, 1, 1], 3))
print(so.numberOfSubarrays([2, 4, 6], 1))
print(so.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
