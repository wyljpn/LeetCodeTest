class Solution:
    def replaceSpace(self, s):
        counter = s.count(' ')

        res = list(s)
        res.extend([' '] * counter * 2)

        left, right = len(s) - 1, len(res) - 1

        while left >= 0:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                res[right-2:right+1] = "%20"
                right -= 3

            left -= 1

        return "".join(res)

    def replaceSpace_2(self, s):
        # join用法：使用指定的str来连接list元素，并且返回字符串
        return "%20".join(s.split(' '))