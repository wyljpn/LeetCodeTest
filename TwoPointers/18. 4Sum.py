
class Solution:
    # 双指针法
    def fourSum(self, nums, target):

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for k in range(i + 1, n):
                if k > i + 1 and nums[k] == nums[k - 1]: continue
                p = k + 1
                q = n - 1

                while p < q:
                    if nums[i] + nums[k] + nums[p] + nums[q] > target:
                        q -= 1
                    elif nums[i] + nums[k] + nums[p] + nums[q] < target:
                        p += 1
                    else:
                        res.append([nums[i], nums[k], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        while p < q and nums[q] == nums[q - 1]: q -= 1
                        p += 1
                        q -= 1
        return res

    def fourSum_2(self, nums, target):

        # use a dict to store value:showtimes
        hashmap = dict()
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        # good thing about using python is you can use set to drop duplicates.
        ans = set()
        # ans = []  # save results by list()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in hashmap:
                        # [1,0,-1,0,-2,2]
                        # 0
                        # [-2, 0, 1, 1] 满足等于0。1出现了两次，但实际上只有1个1。所有要判断每个元素出现的次数不能多于实际的数量。
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if hashmap[val] > count:
                            ans_tmp = tuple(sorted([nums[i], nums[j], nums[k], val]))
                            ans.add(ans_tmp)
        return list(ans)