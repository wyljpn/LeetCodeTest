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
                    # print("False")
                    return False
            # print("True")
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
            # print("s_dict:", s_dict)

            while isSubString(s_dict, t_dict):
                if min_len > (fast - slow + 1):
                    min_len = fast - slow + 1
                    res = s[slow:fast + 1]
                # min_len = min(min_len, fast - slow + 1)
                # print("min_len: ", min_len)
                # res = s[slow:fast+1]
                # print("res:", res)
                s_dict[s[slow]] -= 1
                slow += 1
                # print("after s_dict:", s_dict)

            # print("fast: ", fast)
            # print("slow: ", slow)

        return res if min_len != float("inf") else ""

if __name__ == "__main__":
    so = Solution()
    print(so.minWindow("ADOBECODEBANC", "ABC"))
    print(so.minWindow("a", "a"))
    print(so.minWindow("a", "aa"))
    print(so.minWindow("cabwefgewcwaefgcf", "cae"))
