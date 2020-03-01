class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # see https://leetcode.com/problems/non-decreasing-array/discuss/106885/Simple-Python-solution
        # 把违例的值修正，使其符合nums[i]<nums[i+1]。 所以每次只需要判断nums[i] > nums[i+1]即可。
        count_dec = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count_dec += 1
                if i == 0:
                    nums[i] = nums[i+1]
                elif nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
            if count_dec > 1:
                return False
        return True



    def checkPossibility_1(self, nums):
        count_dec = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count_dec+=1
                # 需要比较下标为i-1, i+1, i+2的数。
                if count_dec > 1 or ((i >= 1 and nums[i-1] > nums[i+1]) and (i+2<len(nums) and nums[i-1] < nums[i+1])):
                    return False
        return True
