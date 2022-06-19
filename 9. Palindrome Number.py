class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # If the number is negative, it's definitely not a Palindrome Number, so return False
        if x < 0:
            return False

        str_x = str(x)
        left_index = 0
        right_index = len(str_x) - 1

        # Compare the digits one by one, return False if they are different
        while left_index < right_index :
            if str_x[left_index] == str_x[right_index]:
                # print(left_index, str_x[left_index])
                # print(right_index, str_x[right_index])
                left_index += 1
                right_index -= 1
            else:
                return False

        # Because all digits are compared same, it's sure that the number is a Palindrome Number, so return True
        return True


    def isPalindrome_2(self, x):
        if x < 0:
            return False

        reversed_number = self.reverseNumber(x)

        if x == reversed_number:
            return True
        else:
            return False


        pass

    def reverseNumber(self, x):
        result = 0
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = int (x / 10)
            # print(result, x)
        return result

if __name__ == "__main__":
    so = Solution()

    # print(so.isPalindrome(121))
    # print(so.isPalindrome(-121))
    # print(so.isPalindrome(10))
    # print(so.isPalindrome(1000021))
    # print(so.isPalindrome(1210021))
    print(so.reverseNumber(123))


    print(so.isPalindrome_2(121))
    print(so.isPalindrome_2(-121))
    print(so.isPalindrome_2(10))
    print(so.isPalindrome_2(1000021))
    print(so.isPalindrome_2(1210021))