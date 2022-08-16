# 76. 最小覆盖子串
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"

class Solution:
    def __init__(self):
        import collections
    # 保存T中的字符
        self.ori = collections.defaultdict(int)
    # 要检查的字符串
        self.cnt = collections.defaultdict(int)

    def cheak(self):
        for key, value in self.ori.items():
            if key not in self.cnt.keys() or self.cnt[key] < value:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        for ti in t:
            self.ori[ti] += 1
        l, r = 0, -1
        length, ansL, ansR = float('inf'), -1, -1
        sLen, tLen = len(s), len(t)
        while r < sLen:
            r += 1
            if r < sLen and s[r] in self.ori.keys():
                self.cnt[s[r]] += 1
            # 检查窗口是否满足
            while self.cheak() and l <= r:
                if r - l + 1 < length:
                    length = r - l + 1
                    ansL = l
                    ansR = l + length
                if s[l] in self.ori.keys():
                    self.cnt[s[l]] -= 1
                l += 1
        return "" if ansL == -1 else s[ansL:ansR]