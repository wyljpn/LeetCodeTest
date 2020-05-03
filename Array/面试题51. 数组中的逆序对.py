class Solution(object):

    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)

        i = l         # 初始化第一个子数组的索引
        j = mid + 1   # 初始化第二个子数组的索引
        pos = l       # 初始归并子数组的索引
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                # (j - (mid + 1))是右边的偏移值。 只有当nums[i] <= nums[j]是，才累加上偏移值。
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1

        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r + 1] = tmp[l:r + 1]
        return inv_count

    def reversePairs(self, nums):
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)


so = Solution()

print(so.reversePairs([7, 5, 6, 4]))
