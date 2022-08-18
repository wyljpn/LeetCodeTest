class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        index = -1
        try:
            index = haystack.index(needle)
        except:
            index = -1
        return index

    def strStr_1(self, haystack, needle):
        return haystack.find(needle)

    def strStr_2(self, haystack, needle):
        for i in range(len(haystack) - len(needle) - 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


    def strStr_3(self, haystack, needle):
        def kmp(str_):
            b, prefix = 0, [0]
            for i in range(1, len(str_)):
                while b > 0 and str_[i] != str_[b]:
                    b = prefix[b - 1]
                if str_[b] == str_[i]:
                    b += 1
                else:
                    b = 0
                prefix.append(b)
            return prefix

        str_ = kmp(needle + '#' + haystack)
        n = len(needle)
        if n == 0:
            return n
        for i in range(n + 1, len(str_)):
            if str_[i] == n:
                return i - 2 * n
        return -1

    # KMP
    # 前缀表全部都-1的方案
    def strStr_4(self, haystack, needle):

        a = len(needle)
        b = len(haystack)

        if a == 0:
            return 0

        next = self.getNext(needle)
        # p是用来指向needle当前正在比较元素的index
        p = -1

        # 遍历要查找的字符串
        for j in range(b):

            # 比较needle[p + 1] 与 haystack[j]
            # 比较在needle中的元素，不包含第一个元素(p为-1的情况)。
            # 因为比较第一个元素，即使不匹配，也不用回退。
            # p==-1用来作为终止回退的条件。
            while p >= 0 and haystack[j] != needle[p + 1]:  # 回退完了之后，是比较 next[p] + 1的位置，补上了统一减去的1。
                p = next[p]

            if haystack[j] == needle[p + 1]:
                p += 1

            # 匹配整个字串的时候，就返回其在字符串的index
            if p == a - 1:
                return j - a + 1

        return -1

    def getNext(self, needle):
        next = ['' for i in range(len(needle))]
        k = -1
        next[0] = k

        for i in range(1, len(needle)):
            while k > -1 and needle[k + 1] != needle[i]:
                k = next[k]

            if needle[k + 1] == needle[i]:
                k += 1

            next[i] = k

        return next


    # KMP
    # 直接使用前缀表方案
    def strStr_5(self, haystack, needle):

        a = len(needle)
        b = len(haystack)

        if a == 0:
            return 0

        next = self.getNext(needle)
        # p是用来指向needle当前正在比较元素的index
        p = 0

        # 遍历要查找的字符串
        for j in range(b):

            # 比较needle[p]（注意，与统一减一的方案不同） 与 haystack[j]
            # 比较在needle中的元素，不包含第一个元素(p为0的情况)。
            # 因为比较第一个元素，即使不匹配，也不用回退。
            # p==0用来作为终止回退的条件。
            while p >= 1 and haystack[j] != needle[p]:
                p = next[p - 1]

            if haystack[j] == needle[p]:
                p += 1

            # 匹配整个字串的时候，就返回其在字符串的index
            if p == a:
                return j - a + 1

        return -1

    # 使用前缀表当成Next
    def getNext_2(self, needle):
        next = ['' for i in range(len(needle))]
        k = 0
        next[0] = k

        for i in range(1, len(needle)):
            while k > 0 and needle[k] != needle[i]:
                k = next[k - 1]

            if needle[k] == needle[i]:
                k += 1

            next[i] = k

        return next


so = Solution()

print(so.strStr("hello", "ll"))
print(so.strStr("aaaaa", "bba"))
print(so.strStr("mississippi", "issip"))

print(so.strStr_3("hello", "ll"))
print(so.strStr_3("aaaaa", "bba"))
print(so.strStr_3("mississippi", "issip"))
print(so.strStr_3("mississippi", ""))
