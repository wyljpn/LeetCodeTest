import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        cnt = 0
        num_list = []
        for k in c:
            # print(k, c[k])
            if c[k] == cnt:
                num_list.append(k)
            elif c[k] > cnt:
                cnt = c[k]
                num_list = [k]
        # print("num_list", num_list)
        len_list = []
        for num in num_list:
            # print("index", nums.index(num), nums[::-1].index(num))

            len_list.append(len(nums) - nums.index(num) - nums[::-1].index(num))
        # print("len_list", len_list)
        return min(len_list)


    # see https://leetcode.com/problems/degree-of-an-array/discuss/124317/JavaC%2B%2BPython-One-Pass-Solution
    # 
    def findShortestSubArray_1(self, nums):
        first, count, res, degree = {}, {}, 0, 0
        for i, a in enumerate(nums):
            first.setdefault(a, i)
            count[a] = count.get(a, 0) + 1
            if count[a] > degree:
                degree = count[a]
                res = i - first[a] + 1
            elif count[a] == degree:
                res = min(res, i - first[a] + 1)
        return res


so = Solution()
print(so.findShortestSubArray([1, 2, 2, 3, 1]))
print(so.findShortestSubArray([1,2,2,3,1,4,2]))