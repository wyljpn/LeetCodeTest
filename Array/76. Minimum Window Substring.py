# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        def isSubString(s_dict, t_dict):

            for key, value in t_dict.items():
                if s_dict[key] < value:
                    return False
            return True

        from collections import defaultdict
        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1

        s_dict = defaultdict(int)

        slow = 0
        min_len = float("inf")
        res = ""

        for fast in range(len(s)):
            s_dict[s[fast]] += 1

            while isSubString(s_dict, t_dict):
                if min_len > (fast - slow + 1):
                    min_len = fast - slow + 1
                    res = s[slow:fast + 1]
                s_dict[s[slow]] -= 1
                slow += 1

        return res if min_len != float("inf") else ""


    def minWindow_2(self, s, t):
        needDict = {}
        for char in t:
            if char not in needDict.keys():
                needDict[char] = 1
            else:
                needDict[char] += 1
        needLen = len(t)
        # print("needDic: ", needDict)

        slow = 0
        minLen = float("inf")
        res = ""

        for fast in range(len(s)):
            if s[fast] in needDict.keys():
                if needDict[s[fast]] > 0:
                    needLen -= 1
                needDict[s[fast]] -= 1

            # print("needDict: ", needDict)
            while needLen == 0:
                # print("slow: ", slow)
                # print("fast: ", fast)
                # print("minLen: ", minLen)
                # print("needLen: ", needLen)
                if minLen > (fast - slow + 1):
                    minLen = fast - slow + 1
                    res = s[slow:fast+1]
                #     print("res: ", res)
                # print("s[slow]: ", s[slow])
                if s[slow] in needDict.keys():
                    if needDict[s[slow]] == 0:
                        needLen += 1
                    needDict[s[slow]] += 1

                # print("after needDict: ", needDict)
                slow += 1

        return res if minLen != float("inf") else ""


if __name__ == "__main__":
    so = Solution()
    print(so.minWindow("ADOBECODEBANC", "ABC"))
    print(so.minWindow_2("ADOBECODEBANC", "ABC"))
    print(so.minWindow("a", "a"))
    print(so.minWindow_2("a", "a"))
    print(so.minWindow("a", "aa"))
    print(so.minWindow_2("a", "aa"))
    print(so.minWindow("cabwefgewcwaefgcf", "cae"))
    print(so.minWindow_2("cabwefgewcwaefgcf", "cae"))
    print(so.minWindow("bba", "ab"))
    print(so.minWindow_2("bba", "ab"))
