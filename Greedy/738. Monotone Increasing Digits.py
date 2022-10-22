class Solution:
    def monotoneIncreasingDigits(self, n):

        a = list(str(n))

        for i in range(len(a)-1, 0, -1):
            if a[i] < a[i-1]:
                a[i-1] = str(int(a[i-1]) - 1)
                a[i:] = '9' * (len(a) - i)

        return int("".join(a))

    def monotoneIncreasingDigits2(self, n):

        a = list(str(n))

        flag = len(a)
        for i in range(len(a) - 1, 0, -1):
            if a[i] < a[i - 1]:
                a[i-1] = str(int(a[i-1]) - 1)
                flag = i

        a[flag:] = '9' * (len(a) - flag)

        return int("".join(a))

if __name__ == "__main__":
    so = Solution()
    print(so.monotoneIncreasingDigits(10))
    print(so.monotoneIncreasingDigits(1234))
    print(so.monotoneIncreasingDigits(332))
    print(so.monotoneIncreasingDigits2(10))
    print(so.monotoneIncreasingDigits2(1234))
    print(so.monotoneIncreasingDigits2(332))