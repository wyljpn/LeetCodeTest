class Solution:
    def lemonadeChange(self, bills):

        five = 0
        ten = 0
        twenty = 0

        for i in bills:
            if i == 5:
                five += 1
                continue
            elif i == 10:
                if five >= 1:
                    ten += 1
                    five -= 1
                else:
                    return False
            elif i == 20:
                if ten >= 1 and five >= 1:
                    twenty += 1
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    twenty += 1
                    five -= 3
                else:
                    return False
        # print("five: ", five)
        # print("ten: ", ten)
        # print("twenty: ", twenty)
        return True



if __name__ == "__main__":
    so = Solution()
    print(so.lemonadeChange([5,5,5,10,20]))
    print(so.lemonadeChange([5,5,10,10,20]))