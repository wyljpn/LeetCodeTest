# You are given an array nums consisting of positive integers.
#
# You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.
#
# Return the number of distinct integers in the final array.

# Example 1:
#
# Input: nums = [1,13,10,12,31]
# Output: 6
# Explanation: After including the reverse of each number, the resulting array is [1,13,10,12,31,1,31,1,21,13].
# The reversed integers that were added to the end of the array are underlined. Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
# The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).

# Example 2:
#
# Input: nums = [2,2,2]
# Output: 1
# Explanation: After including the reverse of each number, the resulting array is [2,2,2,2,2,2].
# The number of distinct integers in this array is 1 (The number 2).

class Solution:
    def countDistinctIntegers(self, nums):

        def reverseInt(num):

            tmp = 0

            while num > 0:
                res = num % 10

                tmp = tmp * 10 + res

                num = num // 10

            return tmp

        n = len(nums)
        i = 0

        while i < n:
            reversedNum = reverseInt(nums[i])
            nums.append(reversedNum)

            i += 1

        # print(nums)

        result = len(set(nums))

        return result


    def reverseInt(self, num):

        tmp = 0

        while num > 0:
            res = num % 10
            print("res: ", res)
            tmp = (tmp * 10) + res
            print("tmp: ", tmp)
            num = num // 10
            print("num: ", num)

        return tmp

if __name__ == "__main__":

    so = Solution()

    print(so.countDistinctIntegers([1,13,10,12,31]))
    print(so.countDistinctIntegers([2,2,2]))

    # print(so.reverseInt(13))