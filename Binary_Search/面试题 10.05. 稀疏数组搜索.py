# 面试题 10.05. 稀疏数组搜索
# 稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
#
# 示例1:
#
#  输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
#  输出：-1
#  说明: 不存在返回-1。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sparse-array-search-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):

    def findString(self, words, s):
        if not words:
            return -1
        left, right = 0, len(words) - 1
        while left <= right:
            while left <= right and len(words[left]) == 0:
                left += 1
            while left <= right and len(words[right]) == 0:
                right -= 1
            mid = left + (right - left) // 2
            while mid < right and len(words[mid])==0:
                mid += 1
            if words[mid] == s:
                return mid
            elif words[mid] > s:
                right = mid - 1
            else:
                left = mid + 1
        return -1


so = Solution()

print(so.findString(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ta"))
print(so.findString(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ball"))
print(so.findString(["AX zEfzhxdXXbeCQOKa", "aLRAEYPIZokU", "giqyZpvcOHdfPpRqHAD", "mhQf", "uwIPRHFftk"],
                    "btRVwblGdpLTtSLbjFzB"))
print(so.findString(
    ["", "", "", "", "AbHSZkLKTnHBbchUaS", "", "", "", "", "", "", "", "", "", "", "", "Ag kFlfSmsAEMy", "", "AsKLCqP",
     "", "", "", "", "", "AwNHxnNNZG", "", "", "", "", "", "", "", "BPwnIg", "", "CTZVBhsbvQpKHn", "DbWXiVetWyFeDu", "",
     "", "", "", "DdVm", "", "", "", "", "EIXK", "EUzGOV", "", "FBLOHPrpE", "GHMqgmMCXLkEBgU", "", "HPDGLlVDt", "", "",
     "", "", "", "", "HfF", "", "", "", "ILzzRaXUzNieYll", "", "", "", "", "", "", "", "", "IXO", "", "", "", "",
     "JMsO", "", "", "", "", "", "", "", "", "", "", "", "JNqzgSHitHRhdauLMcJ", "", "JZkNLIvaG", "", "",
     "KwRVFXYVJiueHvDHRTaJ", "", "", "LDTWBS", "", "", "", "", "", "", "LYN", "", "", "", "", "", "", "",
     "LpgNAXXV cWNYTwxo", "", "", "", "", "", "", "", "", "", "LxWJTErsIjyXjfCqrK", "", "", "", "", "", "", "", "",
     "MlJUQNiISaxtt", "", "", "", "", "", "", "", "", "", "", "O", "", "", "", "", "", "", "", "OHyIQptaYAfinbkjT", "",
     "", "", "", "", "", "", "", "", "", "", "OcQIESYXEmdykm", "", "", "", "", "", "", "", "", "Ol utzavtJOrPIK", "",
     "", "", "", "QLy", "", "", "", "", "", "QQZriWTlYYJgdlWl", "", "", "", "", "", "QhHySgWDIJwFtYP", "", "", "", "",
     "", "", "", "", "", "QiqwcedXKkVHDulp", "", "", "", "", "", "QtSvWSREnaYrrscc", "RHHeBMEnG nUX", "", "", "", "",
     "", "", "", "", "", "S", "", "", "", "", "", "", "", "", "", "SoULoFHOumjYMArBdiW", "", "", "", "",
     "SqHyxrJVNkrNaZG", "", "", "", "", "", "", "", "ThyUiuy", "", "", "Tu ac", "", "", "", "", "", "", "", "", "",
     "UGoOqhdXVzKl", "", "", "", "", "UbmA", "", "", "", "", "", "", "", "", "", "", "UsJhUmDujiOTntftsx", "", "", "",
     "", "", "", "", "", "", "", "V", "", "", "", "", "", "", "", "WEHisFZW wgmmVL", "", "", "", "", "", "", "", "", "",
     "", "", "WayOichMZsXpvJF", "", "WxVmzLgGjGlZOJwdzRd", "", "", "WzMjbVe WqjHOZJi", "", "", "", "", "", "", "", "",
     "", "", "", "XBVQZDHQT", "", "", "", "", "", "XMnsPtB AuMzDv", "", "XRNgMvqmhfjSfVVOP", "", "", "", "", "", "", "",
     "", "", "XYNh", "", "", "", "YfT", "", "", "", "", "", "", "", "", "", "", "", "amPIKYDmkUtUtFznRSvy", "", "", "",
     "", "", "", "", "", "", "bSs H MHwtgkOUzc", "", "", "", "cZhtYPrq ZpxZ", "", "", "", "", "", "", "dUGjmZGq", "e",
     "", "", "", "", "", "", "", "", "", "eWp", "epctu", "", "", "", "", "", "", "", "", "ezTPGIKrUmY", "", "", "", "",
     "", "", "", "", "", "", "fDnxFNxYyzUdQLc", "", "", "", "", "", "", "fFq", "", "", "", "", "", "", "", "", "", "",
     "fVjbEkHHU", "", "", "", "", "", "", "fux", "", "", "", "", "", "", "", "", "", "", "fwNIhmjYGktBo", "", "", "",
     "", "", "", "gEw", "", "", "hCisHtVxXZLjazN", "", "", "iqtlVbWLc", "", "", "jgLIRdgwDIaXioxoQkJn", "", "jpfhmJLfe",
     "", "", "", "kJEFz", "", "", "", "", "", "", "", "", "", "", "kKGFNPRtWNMY", "", "", "", "", "", "", "", "kXsm YJ",
     "", "", "", "kxjNfp c", "", "", "", "", "lnHVOerQcvgQEbBH", "", "", "", "", "", "mBsZUwwGmIsTwBUG", "",
     "mDMENtWiZwu", "", "miuxyF VvYebav", "", "", "", "", "", "nMWP", "", "", "", "", "", "", "", "", "", "", "",
     "nVbrbTsffMvICzx", "", "", "", "nYQuyy", "", "neMPLcFrptsISrhXBWe", "", "", "", "", "", "", "", "", "", "oAhJcIL",
     "", "", "", "", "ptybFCyrvqgy", "", "", "", "qVMPHyOgzIexxZ", "", "", "", "", "", "", "", "qvxuleCVWTYeboMK",
     "qyJLPQMBUuEEkhI", "", "", "", "", "", "", "", "", "", "", "rOsUPq", "", "", "", "sp v", "tjABXGFKaX", "", "", "",
     "", "", "", "", "", "uCFtpnikffzpIGynu", "", "", "uUOuBVKFxs", "", "", "", "", "", "", "ukVV", "", "", "", "",
     "uoRyNsvADRrPlF", "", "", "vJEsAKrSc jrBnvb", "", "", "", "", "", "", "", "", "", "", "wKjM", "", "", "", "", "",
     "", "", "", "wfWltxcuOFs", "", "", "", "", "", "", "", "wrjXviwslafTEBrLBDcQ", "", "", "", "", "", "", "", "", "",
     "", "xqhYBOAEpUzGUDG", "", "", "", "", "", "", "", "", "", "", "y", "", "yEvRmNbkvfELjCvG", "", "", "", "", "", "",
     "z NBqViMo", "", "", "", "zhEOGXTiOsTMbzW", "", "", "", "", "", "zuaVLjhQhNdg"], "WEHisFZW wgmmVL"))
