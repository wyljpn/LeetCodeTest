# Example 1:
#
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:
#
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:
#
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index = len(s) - 1
        t_index = len(t) - 1

        s_backspace = 0
        t_backspace = 0

        while s_index >= 0 or t_index >= 0:

            while s_index >= 0:
                if s[s_index] == "#":
                    s_backspace += 1
                    s_index -= 1
                # 如果当前不是"#"，但是后一个字符是"#"的时候，继续检查上一个字符
                elif s_backspace > 0:
                    s_backspace -= 1
                    s_index -= 1
                else:
                    break

            while t_index >= 0:
                if t[t_index] == "#":
                    t_backspace += 1
                    t_index -= 1
                # 如果当前不是"#"，但是后一个字符是"#"的时候，继续检查上一个字符
                elif t_backspace > 0:
                    t_backspace -= 1
                    t_index -= 1
                else:
                    break

            if s_index >= 0 and t_index >= 0:
                if s[s_index] != t[t_index]:
                    return False
            elif s_index >= 0 or t_index >= 0:
                return False

            s_index -= 1
            t_index -= 1

        return True



if __name__ == "__main__":
    so = Solution()
    print(so.backspaceCompare("ab#c", "ad#c"))  # True
    print(so.backspaceCompare("ab##", "c#d#"))  # True
    print(so.backspaceCompare("a#c", "b"))      # False
    print(so.backspaceCompare("##c", "c"))      # True
    print(so.backspaceCompare("bxj##tw", "bxj###tw"))  # False




