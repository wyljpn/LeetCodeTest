class Solution:
    def partitionLabels(self, s):
        from collections import defaultdict

        dic = defaultdict(int)

        # 记录最后一个出现时候的index
        for i in range(len(s)):
            dic[s[i]] = i

        result = []
        start = 0
        end = dic[s[0]]

        for i in range(len(s)):
            # 到了当前段的末尾
            if i == end:
                # print(s[start:end+1])
                result.append(end - start + 1)
                # 边缘处理。在最后一个位置时，就不用设置start和end了。
                if i + 1 < len(s):
                    start = i + 1
                    end = dic[s[i+1]]
            # 需要延长当前段
            elif dic[s[i]] > end:
                end = dic[s[i]]

        return result


    def partitionLabels2(self, s):
        from collections import defaultdict

        dic = defaultdict(int)

        # 记录最后一个出现时候的index
        for i in range(len(s)):
            dic[s[i]] = i

        result = []
        start = 0
        end = 0

        for i in range(len(s)):
            # 尝试扩展当前段
            end = max(dic[s[i]], end)

            if end == i:
                result.append(end - start + 1)
                start = i + 1

        return result


    def partitionLabels3(self, s):
        # 把a-z的index映射到0-25
        hash = [0 for _ in range(26)]
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] = i
        result = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord('a')])
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result




if __name__ == "__main__":
    so = Solution()
    print(so.partitionLabels("ababcbacadefegdehijhklij"))
    print(so.partitionLabels("eccbbbbdec"))
    print(so.partitionLabels("caedbdedda"))  # 某个字母只出现一次的时候，出现在头
    print(so.partitionLabels("eaaaabaaec"))  # [9, 1] 某个字母只出现一次的时候，出现在尾
    print(so.partitionLabels2("ababcbacadefegdehijhklij"))
    print(so.partitionLabels2("eccbbbbdec"))
    print(so.partitionLabels2("caedbdedda"))  # 某个字母只出现一次的时候，出现在头
    print(so.partitionLabels2("eaaaabaaec"))  # [9, 1] 某个字母只出现一次的时候，出现在尾