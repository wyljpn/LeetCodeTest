class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 未遇上0之前，相当于给自己重新赋值。
        # 遇上0之后，zero标志的是0的位置。 此后进行与0进行值交换的操作。
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    # 只保留不为零的元素。然后在末尾补0
    def moveZeroes_1(self, nums):
        count = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        nums += [0] * count

    # 删除为0的元素，并且马上在末尾补0
    def moveZeroes_2(self, nums):
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                end -= 1
            # 只有nums[i]不为0的时候，i才自增。因为del nums[i]之后，nums[i]变成了原先nums[i+1]
            else:
                i += 1

    # 快慢指针
    def moveZeroes_3(self, nums):
        slow = 0
        fast = 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                if fast != slow:
                    nums[fast] = 0
                slow += 1
            fast += 1


so = Solution()
print(so.moveZeroes([0, 1, 0, 3, 12]))
