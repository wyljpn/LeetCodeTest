class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                # 标记下标
                dic[nums[i]] = i
            else:
                # 下标之差
                if i - dic[nums[i]] <= k:
                    return True
                else:
                    # 更新下标
                    dic[nums[i]] = i
        return False

    # 思路一样，写法更优雅
    def containsNearbyDuplicate_2(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False



so = Solution()
# print(so.containsNearbyDuplicate([1, 2, 3, 1], 3))
# print(so.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(so.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
