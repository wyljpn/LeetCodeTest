class Solution(object):

    # Approach 1: Brute Force
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        def allUnique(s, start, end):
            # print(s[start: end])
            return len(s[start: end]) == len(set(s[start: end]))

        if not s:
            return 0

        ans = 1
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if allUnique(s, i, j + 1):
                    # print(s[i:j+1])
                    ans = max(ans, j - i + 1)
                else:
                    break
        return ans

    # Approach 2: Sliding Window
    def lengthOfLongestSubstring_1(self, s):
        n = len(s)
        used = set()
        ans = 0
        start, end = 0, 0
        while start < n and end < n:
            if not s[end] in used:
                used.add(s[end])
                ans = max(ans, end - start + 1)
                end += 1
            else:
                used.remove(s[start])
                start += 1
        return ans

    # Approach 3: Sliding Window Optimized
    def lengthOfLongestSubstring_2(self, s):
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

        return max_length


so = Solution()

print(so.lengthOfLongestSubstring("abcabcbb"))
print(so.lengthOfLongestSubstring("bbbbb"))
print(so.lengthOfLongestSubstring("pwwkew"))
print(so.lengthOfLongestSubstring(" "))
print(so.lengthOfLongestSubstring(""))
print(so.lengthOfLongestSubstring("au"))

print(so.lengthOfLongestSubstring_1("abcabcbb"))
print(so.lengthOfLongestSubstring_1("bbbbb"))
print(so.lengthOfLongestSubstring_1("pwwkew"))
print(so.lengthOfLongestSubstring_1(" "))
print(so.lengthOfLongestSubstring_1(""))
print(so.lengthOfLongestSubstring_1("au"))
