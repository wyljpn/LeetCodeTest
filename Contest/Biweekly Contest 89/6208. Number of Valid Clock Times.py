class Solution:
    def countTime(self, time):

        result = 1
        if time[4] == "?":
            result *= 10

        if time[3] == "?":
            result *= 6

        if time[0] == "?" and time[1] != "?":
            if time[1] < "4":
                result *= 3
            else:
                result *= 2
        elif time[0] == "?" and time[1] == "?":
            result *= 24

        if time[0] != "?" and time[1] == "?":
            if time[0] <= "1":
                result *= 10
            else:
                result *= 4
        # elif time[0] != "?" and time[1] != "?":


        return result

if __name__ == "__main__":
    so = Solution()
    print(so.countTime("?5:00"))
    print(so.countTime("0?:0?"))
    print(so.countTime("??:??"))
    print(so.countTime("?4:22"))

