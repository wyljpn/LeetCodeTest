class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 限制条件：一个组合中，允许有相同的元素,[-1, -1, 2]。但是不允许有完全相同的组合, [-1, -1, 2] 和 [-1, -1, 2]。
        # 在[-1, -1, 2, 2]中，result中只允许一个[-1, -1, 2]
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            left = i + 1
            right = n - 1

            if nums[i] > 0:  # 剪枝
                break

            if i >= 1 and nums[i] == nums[i - 1]:  # 去重
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]:  # 去重
                        left += 1
                    while left != right and nums[right] == nums[right - 1]:  # 去重
                        right -= 1

                    left += 1
                    right -= 1

        return ans
