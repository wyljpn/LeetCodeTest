class Solution(object):
    def maxArea(self, height):

        left_x = 0
        right_x = len(height) - 1
        res = 0

        while left_x < right_x:
            res = max(res, (right_x - left_x) * min(height[left_x], height[right_x]))
            if height[left_x] <= height[right_x]:
                left_x += 1
            else:
                right_x -= 1

        return res


so = Solution()

print(so.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(so.maxArea([1,5,4,6,7]))
print(so.maxArea([1,5]))
print(so.maxArea([9,4,3,5,9]))
print(so.maxArea([9,4,0,9]))
print(so.maxArea([2,3,4,5,18,17,6]))
