# You are given an array of equal-length strings words. Assume that the length of each string is n.
#
# Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.
#
# For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
# All the strings in words have the same difference integer array, except one. You should find that string.
#
# Return the string in words that has different difference integer array.
#
# Example 1:
#
# Input: words = ["adc","wzy","abc"]
# Output: "abc"
# Explanation:
# - The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
# - The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
# - The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1].
# The odd array out is [1, 1], so we return the corresponding string, "abc".
# Example 2:
#
# Input: words = ["aaa","bob","ccc","ddd"]
# Output: "bob"
# Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].
#
# Constraints:
#
# 3 <= words.length <= 100
# n == words[i].length
# 2 <= n <= 20
# words[i] consists of lowercase English letters.


class Solution:
    # 如果一个值跟同时和之前一个item和之后一个item不同，那么它就是target
    # 边界值：第一个word和最后一个word
    def oddString(self, words):

        # 遍历字符的长度
        for i in range(1, len(words[0])):

            # 遍历数组的长度
            for j in range(len(words)-1):

                # 边界值处理：第一个. 比较第二个和第三个
                if j == 0:
                    if (ord(words[0][i]) - ord(words[0][i-1])) != (ord(words[1][i]) - ord(words[1][i-1])) and (ord(words[0][i]) - ord(words[0][i-1])) != (ord(words[2][i]) - ord(words[2][i-1])):
                        return words[0]
                    continue

                if (ord(words[j][i]) - ord(words[j][i-1])) != (ord(words[j-1][i]) - ord(words[j-1][i-1])) and (ord(words[j][i]) - ord(words[j][i-1])) != (ord(words[j+1][i]) - ord(words[j+1][i-1])):
                    return words[j]

        # 边界值处理：返回最后一个
        return words[-1]

if __name__ == "__main__":
    so = Solution()
    print(so.oddString(["adc","wzy","abc"]))
    print(so.oddString(["aaa","bob","ccc","ddd"]))
    print(so.oddString(["sba","ccc","ddd"])) # 第一个
    print(so.oddString(["ccc","ddd","tmd"])) # 最后一个


