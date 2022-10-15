#
#
# Analphabetical continuous stringis a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string"abcdefghijklmnopqrstuvwxyz".
# * For example,"abc"is an alphabetical continuous string, while"acb"and"za"are not.
# Given a strings consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.
#
# Example 1:
# Input: s = "abacaba"
# Output: 2
# Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
# "ab" is the longest continuous substring.
# Example 2:
# Input: s = "abcde"
# Output: 5
# Explanation: "abcde" is the longest continuous substring.
#
# Constraints:
# * 1 <= s.length <= 105
# * s consists of only English lowercase letters.


class Solution:
    def longestContinuousSubstring(self, s):
        alphabetical_str = "abcdefghijklmnopqrstuvwxyz"
        point = alphabetical_str.index(s[0])
        result = 0

        flag = point
        for i in range(len(s)):
            # print("point:", point)

            if point >= len(alphabetical_str):
                point = alphabetical_str.index(s[i])
                flag = point

            if point < len(alphabetical_str) and s[i] == alphabetical_str[point]:
                point += 1
                result = max(result, point - flag)
            else:
                # print("s[i]:", s[i])
                point = alphabetical_str.index(s[i])
                # print("alphabetical_str[point]:", alphabetical_str[point])
                flag = point

        return result


if __name__ == "__main__":
    so = Solution()

    print(so.longestContinuousSubstring("abacaba"))  # 2
    print(so.longestContinuousSubstring("abcde"))    # 5
    print(so.longestContinuousSubstring("bcdahlz"))  # 3
    print(so.longestContinuousSubstring("z"))        # 1
    print(so.longestContinuousSubstring("qrstuabc")) # 5
    print(so.longestContinuousSubstring("wxyzab"))   # 4
    print(so.longestContinuousSubstring("yzabcdefg"))  # 7
