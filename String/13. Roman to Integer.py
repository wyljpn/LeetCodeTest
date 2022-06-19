class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dic = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500,
               "CM": 900, "M": 1000}
        i = 0
        while i < len(s):
            # Two characters in the dictionary, add its value to the result.
            # Tip: we can specify end index larger than its length.
            if dic.get(s[i:i+2], -1) != -1:
                res += dic.get(s[i:i+2])
                i += 2
            else:
                # Single character, and its value to the result.
                res += dic.get(s[i])
                i +=1

        return res

    def romanToInt_1(self, s):
        dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        num, pre = 0, 1000
        for i in [dic[j] for j in s]:
            num, pre = num + i - 2 * pre if i > pre else num + i, i
        return num

    def romanToInt_2(self, s):
        dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res, p = 0, 'I'
        # Reverse string, then calculate.
        # If current value larger than previous, then add it to result
        # else subtract it from result
        for c in s[::-1]:
            res, p = res + dic[c] if dic[c] >= dic[p] else res - dic[c], c
        return res


so = Solution()
print(so.romanToInt("III"))
print(so.romanToInt("IV"))
print(so.romanToInt("IX"))
print(so.romanToInt("LVIII"))
print(so.romanToInt("MCMXCIV"))
