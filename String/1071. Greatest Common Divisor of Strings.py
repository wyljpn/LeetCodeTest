class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 == str2:
            return str1
        cnt = 0
        for i in range(1, min(len(str1), len(str2))+1):
            a = ''.join(str1.split(str1[:i]))
            b = ''.join(str2.split(str2[:i]))
            if '' == a and '' == b and str1[:i] == str2[:i]:
                cnt = i
        # print("cnt", cnt)
        return str1[:cnt]

    # Method 1: imitate gcd algorithm, recursive version.
    #   1.If longer string starts with shorter string, cut off the common prefix part of the longer string; repeat till one is empty, then the other is gcd string;
    #   2.If the longer string does NOT start with the shorter one, there is no gcd string.
    def gcdOfStrings_1(self, str1, str2):
        if not str1 or not str2:
            return str1 if str1 else str2
        # 长的string放在第一个参数
        elif len(str1)< len(str2):
            return self.gcdOfStrings_1(str2, str1)
        #
        elif str1[: len(str2)] == str2:
            return self.gcdOfStrings_1(str1[len(str2):], str2)
        else:
            return ''

    # Method 2: compare substring, iterative version.
    # The length of gcd substring must be the gcd of the lengthes of both string.
    #
    # check if the substring(0, i) of str1 is the divisor string of
    #     1.str1;
    #     2.str2.
    #     Increase i to find its maximum value for gcd string.
    def gcdOfStrings_2(self, str1, str2):
        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)
        d = gcd(len(str1), len(str2))
        return str1[: d] if str1[: d] * (len(str2) // d) == str2 and str2[: d] * (len(str1) // d) == str1 else ''


    # Method 3: Regular Expression.
    #
    # Compute the gcd of the lengthes of the 2 strings, then confirm if the gcd size of the prefix of str1 is actually the gcd of the strings.
    # Note for regex:
    #
    #   1.() to make the string inside as a group;
    #   2.+ is quantifier, which means 1 or more of the group ahead of the +.

    def gcdOfStrings_3(self, str1, str2):
        import re
        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)
        d = gcd(len(str1), len(str2))
        gcd_str = str1[0 : d]
        ptn = '(' + gcd_str + ')+'
        # fullmatch方法与match类似，只不过，该方法搜索的匹配内容必须和搜索的原文一样，否则都认为是未找到。
        return gcd_str if re.fullmatch(ptn, str1) and re.fullmatch(ptn, str2) else ''


so = Solution()

print(so.gcdOfStrings("ABCABC", "ABC"))
print(so.gcdOfStrings("ABABAB", "ABAB"))
print(so.gcdOfStrings("LEET", "CODE"))
print(so.gcdOfStrings("A","A"))