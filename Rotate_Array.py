import collections


class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())

    def rotate2(self, nums, k):
        deque = collections.deque(nums)
        k %= len(nums)
        for _ in range(k):
            deque.appendleft(deque.pop())
        nums[:] = list(deque)

    def rotate3(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


nums = [-1, -100, 3, 99]
k = 2
sol = Solution()
print(sol.rotate(nums, k))
